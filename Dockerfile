FROM python:3.14-slim

WORKDIR /app

# System deps for building some packages
RUN apt-get update && apt-get install -y build-essential libxml2-dev libxslt1-dev zlib1g-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN python -m venv /opt/venv && /opt/venv/bin/pip install --upgrade pip setuptools wheel && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PATH="/opt/venv/bin:$PATH"

CMD ["/opt/venv/bin/python", "-m", "pytest", "-q"]
