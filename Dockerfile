## Use an official base image with Python
##FROM python:3.10
#
## Base Image
#FROM ollama/ollama:latest AS ollama
#
## Pull the Llama3 model inside the Ollama container
#RUN ollama pull llama3
#
## Python Application Image
#FROM python:3.10 AS books_app
#
## Set the working directory
#WORKDIR /app
#
## Install system dependencies
#RUN apt-get update && apt-get install -y curl && \
#    curl -fsSL https://ollama.com/install.sh | sh
#
## Ensure Ollama binary is in PATH
#ENV PATH="/root/.ollama/bin:$PATH"
#
## Preload the Llama3 model during the build
##RUN ollama pull llama3
#
#
## Install Python dependencies
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#
## Copy application code
#COPY . .
#
## Expose ports for API and Ollama
#EXPOSE 8000 11434
#
## Start FastAPI
#CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
#
#
## Start Ollama in the background and then run FastAPI
##CMD ollama serve & sleep 5 && ollama pull llama3 && wait
#CMD ollama serve & sleep 5 && wait
##CMD uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
#
#RUN ollama pull llama3

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