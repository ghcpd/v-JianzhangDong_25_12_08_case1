FROM python:3.14-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY tests/ ./tests/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "-m", "pytest", "tests/"]
