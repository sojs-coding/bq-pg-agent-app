# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Download and install MCP toolbox
RUN curl -O https://storage.googleapis.com/genai-toolbox/v0.22.0/linux/amd64/toolbox && \
    chmod +x toolbox

# Copy the custom tools configuration
COPY tools.yaml .

# Expose port (Cloud Run will set PORT environment variable)
EXPOSE 8080

# Set environment variables (will be overridden by Cloud Run deployment)
ENV BIGQUERY_PROJECT="agentspace-demo-461406"
ENV PG_PROJECT="agentspace-demo-461406"
ENV PG_INSTANCE="instance1"
ENV PG_DB="database"
ENV PG_USER_NAME="postgres"
ENV PG_PASSWORD="Password123!"
ENV PORT=8080

# Start toolbox with custom configuration using PORT environment variable
CMD ["sh", "-c", "./toolbox --tools-file=tools.yaml --address=0.0.0.0 --port=${PORT:-8080}"]
