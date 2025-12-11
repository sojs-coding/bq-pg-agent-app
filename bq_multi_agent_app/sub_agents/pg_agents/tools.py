"""
Tools for PG Agent

This module provides PG-specific tools including:
1. pg_data_retrieval_toolset: MCP toolset for retrieving database information
2. pg_sql_toolset: MCP toolset for executing Postgres SQL statements
"""

import os

from google.adk.tools.mcp_tool.mcp_session_manager import \
    StreamableHTTPConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset

# Get toolbox URL from environment, default to local development
TOOLBOX_URL = os.getenv("TOOLBOX_URL", "http://127.0.0.1:5000")

# PG toolset for executing SQL/BQML statements
pg_sql_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        # MCP endpoint with BQML toolset filter
        url=f"{TOOLBOX_URL}/mcp/pg_sql_toolset",
        headers={}  # Add auth headers if needed
    )
)

# PG toolset for retrieval of data
pg_data_retrieval_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        # MCP endpoint with BQML toolset filter
        url=f"{TOOLBOX_URL}/mcp/pg_data_retrieval_toolset",
        headers={}  # Add auth headers if needed
    )
)

# PG toolset for retrieval of statistics and status
pg_stats_toolset = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        # MCP endpoint with BQML toolset filter
        url=f"{TOOLBOX_URL}/mcp/pg_stats_toolset",
        headers={}  # Add auth headers if needed
    )
)