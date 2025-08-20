import os
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.sql import SQLTools
from agno.storage.sqlite import SqliteStorage
from agno.utils.pprint import pprint_run_response

from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


from sqlalchemy import create_engine
engine = create_engine('sqlite:///./Chinook_SQLite.sqlite')
sql_tools = SQLTools(db_engine=engine)
print(sql_tools)

storage=SqliteStorage(
    table_name="agent_sessions", 
    db_file="agent_storage.db",
)

agent_prompt = """
You are an AI assistant
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


# user_message = "How many artists do we have"
# agent.print_response(user_message)

user_message = "Give me a sample list of artists."
agent.print_response(user_message)
#agent.print_response(user_message, stream=True)

#response = agent.run(user_message, session_id="session_id", stream=False)
# print(response.content)

#response: RunResponse = agent.run(user_message, session_id="session_id", stream=False)
#pprint_run_response(response, markdown=True)