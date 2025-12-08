FROM python:3.14-slim

WORKDIR /app

# Copy project files
COPY . /app

# Create virtual environment and install pinned requirements
RUN python -m venv /opt/venv && \
    /opt/venv/bin/python -m pip install --upgrade pip setuptools wheel && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

CMD ["/opt/venv/bin/python", "-m", "pytest", "-q"]
