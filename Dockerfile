# Use an official base image with Python
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://ollama.com/install.sh | sh


# Ensure Ollama binary is in PATH
ENV PATH="/root/.ollama/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports for API and Ollama
EXPOSE 8000 11434

# Start Ollama in the background and then run FastAPI
CMD ollama serve & uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

RUN sleep 10 && ollama pull tinyllama | sh