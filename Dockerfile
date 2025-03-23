# Use official Python image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Run migrations
CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
