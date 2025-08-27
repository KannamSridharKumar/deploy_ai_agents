import os
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.sql import SQLTools
from agno.storage.agent.postgres import PostgresAgentStorage
#from agno.utils.pprint import pprint_run_response

from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

PG_DATABASE = os.getenv("PG_DATABASE")
PG_USERNAME = os.getenv("PG_USERNAME")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
DATABASE_URL = f"postgresql+psycopg2://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

sql_tools = SQLTools(db_url=DATABASE_URL)
print(sql_tools)


storage = PostgresAgentStorage(
        table_name="agent_sessions",
        db_url=DATABASE_URL,
    )

agent_prompt = """
You are an AI assistant helping customers track their orders.
- Always ask the customer for their tracking ID if they haven’t provided it yet.
- If the tracking ID is missing or invalid, politely ask the customer to provide it again.
- Respond clearly and helpfully with the order status and all other details, including customer name.
"""

agent = Agent(
    name='orders status agent',
    model=OpenAIChat(id='gpt-5-mini'),
    storage=storage,
    markdown=True,
    show_tool_calls=False,
    system_message=agent_prompt,
    tools=[sql_tools],
    add_history_to_messages=True,
    retries=3
)

user_message = "Hi"
agent.print_response(user_message)

user_message = "Whats the status of the order with tracking ID T1000"
agent.print_response(user_message)

user_message = "Sorry, what was my tracking ID?"
agent.print_response(user_message)
#agent.print_response(user_message, stream=True)

#response = agent.run(user_message, session_id="session_id", stream=False)
# print(response.content)

#response: RunResponse = agent.run(user_message, session_id="session_id", stream=False)
#pprint_run_response(response, markdown=True)
