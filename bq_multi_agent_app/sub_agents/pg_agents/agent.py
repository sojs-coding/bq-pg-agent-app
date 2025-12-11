"""
PG Agent for Postgres operations.

This agent specializes in Postgres tasks such as operational, read, write, and update. 
"""

from google.adk.agents import Agent

from .prompts import return_instructions_pg
from .tools import pg_sql_toolset
from .tools import pg_data_retrieval_toolset
from .tools import pg_stats_toolset

root_agent = Agent(
    model='gemini-3-pro-preview',
    name="pg_agent",
    instruction=return_instructions_pg(),
    tools=[
        pg_sql_toolset,      # MCP toolset for Postgres SQL/BQML execution
        pg_data_retrieval_toolset,   # MCP toolset for retrieving database information
        pg_stats_toolset,      # MCP toolset for retrieving stats and status of database
    ],
)