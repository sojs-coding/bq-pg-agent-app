# BigQuery and CloudSQL Agent with Google ADK

A powerful AI-powered data analysis agent that combines Google BigQuery and Google CloudSQL Postgres with the Google Agent Development Kit (ADK) to enable natural language interactions with your data warehouse.

## Quick Start (Local Development)

1. **Authentication**
```bash
gcloud auth application-default login
```

2. **Clone and Setup**
```bash
git clone https://github.com/sojs-coding/bq-pg-agent-app.git
cd bq-pg-agent-app

# Install uv (if not already installed)
# Visit: https://docs.astral.sh/uv/getting-started/installation/

# Install dependencies with uv
uv sync

# Activate environment
source .venv/bin/activate

# Setup MCP Toolbox
cd setup/mcp_toolbox

# Update the script parameters for your OS before running
# Edit install-mcp-toolbox.sh and update:
# - MCP_VERSION: choose the version from https://github.com/googleapis/genai-toolbox/releases
# - MCP_OS: "linux" for Linux, "darwin" for macOS
# - MCP_ARCH: "amd64" for Intel/x64, "arm64" for Apple Silicon
# Example for macOS Apple Silicon: MCP_OS="darwin" MCP_ARCH="arm64"

chmod +x install-mcp-toolbox.sh
./install-mcp-toolbox.sh
cd ../..

# Create CloudSQL (Postgres) database via the Cloud Console https://docs.cloud.google.com/sql/docs/postgres
# Follow the BQML Agent Setup to create a RAG Corpus
# Follow the Vertex Extension Guide below to create a CODE_INTERPRETER_EXTENSION_NAME

# Configure the environment
# ONLY RUN THIS IF YOU HAVE NO .env FILE
cp .env.example .env

# Set the environment variables
export $(cat .env | grep -v '^#' | xargs)

# Run the MCP server with custom configuration
cd setup/mcp_toolbox
./toolbox --tools-file=tools.yaml --port=5000
cd ../..

# Run ADK
uv run adk web
```

## BQML Agent Setup

This section covers setting up the BQML agent with RAG corpus integration for enhanced BigQuery ML capabilities.

### Prerequisites for BQML Agent

In addition to the basic prerequisites, the BQML agent requires:

1. **Additional APIs enabled**:
   - Vertex AI API
   - BigQuery API (already required)
   - Cloud Resource Manager API

2. **Additional permissions** for your account:
   - Vertex AI User
   - BigQuery User
   - BigQuery Data Viewer

3. **Enable required APIs**:
   ```bash
   # Enable required Google Cloud APIs
   gcloud services enable aiplatform.googleapis.com
   gcloud services enable bigquery.googleapis.com
   gcloud services enable cloudresourcemanager.googleapis.com
   ```

### BQML Environment Configuration

After completing the basic setup, configure BQML-specific environment variables:

```bash
# Edit your .env file to include BQML configuration
# The basic setup already covers most variables, add these BQML-specific ones:

# BQML Agent configuration (leave empty initially)
BQML_RAG_CORPUS_NAME=
```

### RAG Corpus Setup

The BQML agent uses a RAG (Retrieval-Augmented Generation) corpus for enhanced BQML documentation access:

```bash
# From the project root directory
uv run python setup/rag_corpus/create_bqml_corpus.py
```

**What this script does:**

1. **Checks for existing corpus**: If `BQML_RAG_CORPUS_NAME` is empty in your `.env` file
2. **Creates new RAG corpus**: Sets up a Vertex AI RAG corpus with text-embedding-005
3. **Ingests BQML documentation**: Downloads and processes Google's BQML documentation from GCS
4. **Updates environment**: Automatically writes the corpus name to your `.env` file

### Expected Output

When the RAG corpus setup runs successfully:

```
Creating new BQML RAG corpus...
Corpus created: projects/123456789/locations/us-west4/ragCorpora/1234567890123456789
BQML_RAG_CORPUS_NAME 'projects/123456789/locations/us-west4/ragCorpora/1234567890123456789' written to /path/to/your/project/.env
Importing files to corpus: projects/123456789/locations/us-west4/ragCorpora/1234567890123456789
Files imported to corpus: projects/123456789/locations/us-west4/ragCorpora/1234567890123456789
```

### Verify BQML Setup

```bash
# Check that BQML_RAG_CORPUS_NAME is now populated
cat .env | grep BQML_RAG_CORPUS_NAME
```

### Region Selection for BQML

**Important**: The BQML setup uses `us-west4` as the default region for Vertex AI RAG because:

1. **Capacity Limitations**: `us-central1` has allowlisting-based access due to capacity limitations
2. **RAG Engine Availability**: `us-west4` has reliable availability for Vertex AI RAG Engine

### Testing BQML RAG Integration

Test the RAG corpus functionality:

```bash
# Test the RAG corpus with sample queries
uv run python setup/rag_corpus/test_rag.py "What BQML model types are available?"
```

## Additional Guides

- [Vertex Extensions Setup Guide](setup/vertex_extensions/VERTEX_EXTENSIONS_GUIDE.md) - Complete guide for setting up Vertex AI Extensions for code interpretation
- [MCP Toolbox Deployment Guide](setup/mcp_toolbox/MCP_TOOLBOX_GUIDE.md) - Deploy MCP toolbox to Google Cloud Run for production use
- [Opentelemetry ADK Setup Guide](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-adk) - Setup Opentelemetry in ADK
- [Opentelemetry Data Collection Guide](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses) - Export Opentelemetry data to BigQuery, GCS, 

## Implementation

This project provides a comprehensive **Multi-Agent System** for BigQuery analytics with advanced data science capabilities.

| Feature | Multi-Agent System |
|---------|-------------------|
| **Directory** | `bq_multi_agent_app/` |
| **Setup Complexity** | Moderate |
| **BigQuery Operations** | ✅ |
| **MCP Protocol Support** | ✅ |
| **Python Data Science** | ✅ |
| **Statistical Analysis** | ✅ |
| **Data Visualization** | ✅ |
| **Multi-Agent Orchestration** | ✅ |
| **Additional Dependencies** | MCP Toolbox |

### Key Benefits

- **Advanced Analytics**: Complete data science workflows with comprehensive analysis and visualizations
- **Multi-Agent Architecture**: Root agent orchestrates specialized sub-agents for different tasks
- **MCP Integration**: Uses Model Context Protocol for standardized BigQuery operations

## Core Features

- 🔍 **Dataset Discovery**: List and explore BigQuery datasets
- 📊 **Table Analysis**: Get detailed schema and metadata information
- 🔎 **SQL Execution**: Execute complex SQL queries through natural language
- 🤖 **AI-Powered**: Uses Gemini 2.5 Flash for intelligent query understanding
- 🔐 **Flexible Authentication**: Multiple authentication methods supported

## Advanced Features

- 🎯 **Multi-Agent Orchestration**: Root agent delegates tasks to specialized sub-agents
- 🐍 **Python Analytics**: Stateful code execution for advanced data science workflows
- 📈 **Data Visualization**: Automated chart generation with matplotlib
- 🧠 **Statistical Analysis**: Comprehensive statistical testing and modeling
- 🔗 **MCP Integration**: Uses Model Context Protocol for BigQuery operations
- 💬 **Conversational Analytics**: Interactive BigQuery exploration via MCP
- 📊 **Time Series Forecasting**: Built-in forecasting capabilities for temporal data
- 📝 **Pre-defined SQL Templates**: Execute common SQL patterns efficiently

## Usage

### Example Interactions

**Basic Operations**
```
"What datasets are available in my project?"
"Show me the schema of the sales_data table"
"Find the top 10 customers by revenue this year"
```

**Advanced Analytics**
```
"Analyze sales trends over the last 12 months and create a visualization"
→ Root agent retrieves data, DS agent creates trend analysis with charts

"Build a predictive model for customer churn"
→ Root agent extracts features, DS agent trains and evaluates model

"Compare revenue across product categories with statistical testing"
→ Root agent queries data, DS agent performs statistical analysis
```

**BQML Operations**
```
"Create a logistic regression model for customer churn prediction"
→ BQML agent queries RAG corpus, generates CREATE MODEL statement

"What BQML model types are available for forecasting?"
→ BQML agent retrieves documentation about ARIMA_PLUS and time series models

"Show me how to evaluate a BQML model"
→ BQML agent provides ML.EVALUATE function documentation and examples

"List existing BQML models in my dataset"
→ Root agent queries BigQuery information schema for ML models
```

## Architecture

### Foundation
The system is built on:
- **Google Agent Development Kit (ADK)**: Framework for building AI agents
- **Gemini 2.5 Flash**: Large language model for natural language understanding
- **Vertex AI**: Google Cloud's AI platform integration

### Multi-Agent System Architecture
```
Root Agent 
├── Conversational Toolset (MCP Toolbox)
│   └── bigquery-conversational-analytics    # Quick insights & answers
├── Data Retrieval Toolset (MCP Toolbox)
│   ├── bigquery-execute-sql                 # Raw data extraction
│   ├── bigquery-list-dataset-ids           # Dataset discovery
│   ├── bigquery-get-dataset-info           # Dataset metadata
│   ├── bigquery-list-table-ids             # Table discovery
│   └── bigquery-get-table-info             # Table schema
├── ML Analysis Toolset (MCP Toolbox)
│   ├── bigquery-forecast                    # TimesFM forecasting
│   └── bigquery-analyze-contribution        # Contribution analysis
├── DS Sub-Agent (ds_agent)
│   ├── Python Code Execution
│   ├── Data Visualization
│   └── Statistical Analysis
└── BQML Sub-Agent (bqml_agent)
    ├── BQML Toolset (MCP)                   # SQL/BQML execution
    ├── RAG Response                         # BQML documentation queries
    └── Model Listing                        # BigQuery ML model discovery
```

#### Four-Path Workflow
The agent intelligently chooses between four approaches:

**PATH 1: Quick Insights (Conversational Analytics)**
- For simple questions and quick answers
- Uses `bigquery-conversational-analytics` directly
- Returns natural language insights

**PATH 2: In-Depth Analysis (Data Retrieval + Data Science)**
- For complex analysis and visualizations
- Uses `bigquery-execute-sql` → `call_data_science_agent`
- Provides full control over data and analysis

**PATH 3: ML Analysis (TimesFM + Contribution Analysis)**
- For forecasting and understanding drivers of change
- Uses `bigquery-forecast` (TimesFM model) and `bigquery-analyze-contribution`
- Quick ML insights without custom model training

**PATH 4: BQML Operations (BigQuery ML)**
- For custom machine learning model operations
- Delegates to BQML sub-agent → BQML toolset + RAG corpus
- Handles model creation, training, evaluation, and documentation

## Project Structure

```
bq-agent-app/
├── pyproject.toml                   # uv package configuration
├── uv.lock                          # Dependency lock file
├── bq_multi_agent_app/              # Multi-Agent System
│   ├── agent.py                     # Root agent with MCP integration
│   ├── tools.py                     # MCP BigQuery tools + agent wrappers
│   ├── prompts.py                   # Root agent instructions
│   └── sub_agents/
│       ├── ds_agents/               # Data Science Agent
│       │   ├── agent.py             # Data science agent
│       │   └── prompts.py           # DS agent instructions
│       └── bqml_agents/             # BigQuery ML Agent
│           ├── agent.py             # BQML agent with RAG integration
│           ├── prompts.py           # BQML agent instructions
│           └── tools.py             # BQML-specific tools (RAG, model listing)
├── setup/                           # Setup and deployment tools
│   ├── mcp_toolbox/                 # MCP Toolbox setup
│   │   ├── install-mcp-toolbox.sh   # Local installation script
│   │   ├── deploy.sh                # Cloud Run deployment
│   │   ├── Dockerfile               # Container definition
│   │   └── MCP_TOOLBOX_GUIDE.md     # Deployment guide
│   ├── rag_corpus/                  # BQML RAG Corpus Setup
│   │   ├── create_bqml_corpus.py    # RAG corpus creation script
│   │   └── test_rag.py              # RAG corpus testing script
│   ├── vertex_extensions/           # Vertex AI Extensions Management
│   │   ├── setup_vertex_extensions.py   # Create extensions
│   │   ├── cleanup_vertex_extensions.py # Clean up extensions
│   │   ├── utils.py                 # Shared utilities
│   │   └── VERTEX_EXTENSIONS_GUIDE.md   # Setup guide
md  # Comprehensive guide
└── README.md
```

## Prerequisites

- **Python 3.11+**
- **uv** package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- **Google Cloud Project** with BigQuery enabled
- **Google Cloud credentials**

## Deployment

The Multi-Agent System requires both the MCP Toolbox and the Agent to be deployed. You can choose to run each component locally or deploy to Cloud Run based on your needs.

### Step 1: Deploy the MCP Toolbox

The MCP Toolbox provides BigQuery connectivity for the agent.

#### Option A: Run MCP Toolbox Locally
```bash
# Create .env file
# ONLY RUN THIS IF YOU HAVE NO .env FILE
cp .env.example .env

# Set environment variables
export $(cat .env | grep -v '^#' | xargs)

# Start the MCP server with custom configuration
cd setup/mcp_toolbox
BIGQUERY_PROJECT=$BIGQUERY_PROJECT ./toolbox --tools-file=tools.yaml --port=5000
```

#### Option B: Deploy MCP Toolbox to Cloud Run
```bash
# Create .env file
# ONLY RUN THIS IF YOU HAVE NO .env FILE
cp .env.example .env

# Set environment variables
export $(cat .env | grep -v '^#' | xargs)

# Setup
cd setup/mcp_toolbox
chmod +x deploy.sh
./deploy.sh

# To deploy using a local `toolbox` binary instead of the release version, run:
# ./deploy.sh local
```
The script will:
- Enable required Google Cloud APIs
- Create a service account with BigQuery permissions
- Build and push the Docker image
- Deploy to Cloud Run with `--allow-unauthenticated`
- Provide the service URL for access
#### **Replace the url for the TOOLBOX_URL with the url provided by the deployment**
#### Check Google Cloud Console -> Cloud Run. Ensure that under Security Tab, `Allow public access` is toggled.

### Step 2: Deploy the Agent

The agent connects to the MCP Toolbox (local or cloud) to provide BigQuery functionality.

#### Option A: Run Agent Locally
```bash
# Create .env file
# ONLY RUN THIS IF YOU HAVE NO .env FILE
cp .env.example .env

# Set environment variables
export $(cat .env | grep -v '^#' | xargs)

uv run adk web  # or uv run adk run
```

#### Option B: Deploy Agent to Cloud Run
```bash
# Create .env file
# ONLY RUN THIS IF YOU HAVE NO .env FILE
cp .env.example bq_multi_agent_app/.env

# Set environment variables
export $(cat .env | grep -v '^#' | xargs)

uv run adk deploy cloud_run \
  --project=your-project-id \
  --region=us-central1 \
  --service_name=bq-agent-app \
  --trace_to_cloud \
  --with_ui \
  ./bq_multi_agent_app
```

After deployment:
- Access your agent at the provided Cloud Run service URL
- The web UI will be available for interactive testing
- Cloud tracing is enabled for monitoring and debugging

#### Option C: Deploy Agent to Agent Engine
```bash
# Set environment variables
export $(cat .env | grep -v '^#' | xargs)

uv run adk deploy agent_engine \
--project=your-project-id \
--region=us-central1 \
--staging_bucket=gs://staging-bucket-id \
--trace_to_cloud \
--display_name=agent-display-name \
--env_file=.env \
./bq_multi_agent_app/
```

Or to update existing Agent Engine:
```bash
# Set environment variables
export $(cat .env | grep -v '^#' | xargs)

uv run adk deploy agent_engine \
--project=your-project-id \
--region=us-central1 \
--staging_bucket=gs://staging-bucket-id \
--trace_to_cloud \
--display_name=agent-display-name \
--env_file=.env \
--agent_engine_id agent-engine-id \
./bq_multi_agent_app/
```

After deployment:
- Agent is deployed to Vertex AI Agent Engine with managed sessions
- Provides programmatic access via the Agent Engine API
- Integrated with Vertex AI ecosystem for enterprise use
- Supports both synchronous and asynchronous operations

To use ADK Web frontend with Agent Engine:
```bash
agent_engine_id="your-agent-engine-id"

adk web --session_db_url=agentengine://${agent_engine_id}
```

### Deployment Combinations

| MCP Toolbox | Agent | Use Case |
|-------------|-------|----------|
| Local | Local | Development and testing |
| Cloud Run | Local | Development with shared toolbox |
| Cloud Run | Cloud Run | Full production deployment |
| Cloud Run | Agent Engine | Enterprise deployment with managed sessions |

**Note**: Ensure your service account has the necessary BigQuery permissions for your project. For advanced MCP configurations, refer to the [official documentation](https://googleapis.github.io/genai-toolbox/how-to/deploy_toolbox/).

## Agent Management
Go to Google Cloud Console and search for Agent Engine. You can do the following:
- Edit
- Delete
- Monitor

## Security Considerations

- Use minimum required permissions
- Store credentials securely
- Review SQL queries executed by agents
- Consider read-only mode for production

## Related Resources

- [Google Agent Development Kit Documentation](https://cloud.google.com/adk)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP Toolbox Cloud Run Deployment Guide](https://googleapis.github.io/genai-toolbox/how-to/deploy_toolbox/)
- [Blog Post: BigQuery meets Google ADK and MCP](https://cloud.google.com/blog/products/ai-machine-learning/bigquery-meets-google-adk-and-mcp)

---

*Built with ❤️ using Google Agent Development Kit, BigQuery, and MCP*
