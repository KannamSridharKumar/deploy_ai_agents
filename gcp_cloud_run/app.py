import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.sql import SQLTools
from agno.storage.agent.postgres import PostgresAgentStorage


from dotenv import load_dotenv
load_dotenv()  

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

PG_DATABASE = os.getenv("PG_DATABASE")
PG_USERNAME = os.getenv("PG_USERNAME")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
DATABASE_URL = f"postgresql+psycopg2://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

sql_tools = SQLTools(db_url=DATABASE_URL)
storage = PostgresAgentStorage(
        table_name="agent_sessions",
        db_url=DATABASE_URL,
        )


AGENT_PROMPT = """
You are an AI assistant helping customers track their orders.
- Always ask the customer for their tracking ID if they haven’t provided it yet.
- If the tracking ID is missing or invalid, politely ask the customer to provide it again.
- Respond clearly and helpfully with the order status and all other details, including customer name.
"""

agent = Agent(
    name="orders status agent",
    model=OpenAIChat(id=os.getenv("AGNO_MODEL_ID", "gpt-4o-mini")),
    storage=storage,
    markdown=False,
    show_tool_calls=False,
    system_message=AGENT_PROMPT,
    tools=[sql_tools],
    add_history_to_messages=True,
    retries=3,
)

app = FastAPI(title="Order Tracking AI Agent", description="To check order status", version="1.0")

class ChatIn(BaseModel):
    message: str = Field(description="Customer message")
    #session_id: str

class ChatOut(BaseModel):
    response: str  = Field(description="Agent response")

@app.get("/", status_code=200)
async def root():
    return {"message": "The order tracking AI Agent is up & running."}

@app.post("/chat", response_model=ChatOut)
def chat(body: ChatIn):
    try:
        response: RunResponse = agent.run(body.message, stream=False)
        #response: RunResponse = agent.run(body.message, session_id=body.session_id, stream=False)
        return ChatOut(response=response.content, markdown=True)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {e}")