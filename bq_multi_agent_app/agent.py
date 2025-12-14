"""
BigQuery Multi-Agent Application - Root Agent

This is the main agent that orchestrates BigQuery data retrieval and data science analysis.
It uses MCP for BigQuery operations and ADK for data science code execution.
"""

from datetime import date

from google.adk.agents import Agent
from google.adk.tools import load_artifacts

from .prompts import return_instructions_root
from .sub_agents import bqml_agent
from .sub_agents import pg_agent
from .tools import call_data_science_agent
from .tools import bq_conversational_toolset
from .tools import bq_data_retrieval_toolset
from .tools import bqml_analysis_toolset

date_today = date.today()

root_agent = Agent(
    model='gemini-2.5-pro',
    name="bigquery_ds_agent",
    global_instruction=(
        f"""
        You are a Data Science, BigQuery Analytics, and Postgres CloudSQL Multi Agent System.
        Today's date: {date_today}

        Follow the detailed instructions provided to discover schema and execute analysis.
        """
    ),
    instruction=return_instructions_root(),
    sub_agents=[bqml_agent, pg_agent],
    tools=[
        bq_conversational_toolset,     # BigQuery conversational analytics
        bq_data_retrieval_toolset,     # BigQuery data retrieval and schema tools
        bqml_analysis_toolset,        # BigQuery ML analysis tools
        call_data_science_agent,    # Data science analysis with code execution
        load_artifacts,             # Load local files for analysis
    ],
)
