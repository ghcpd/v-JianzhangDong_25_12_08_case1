FROM python:3.14-slim

WORKDIR /app

# Install OS deps for potential wheels
RUN apt-get update && apt-get install -y build-essential libxml2-dev libxslt1-dev libffi-dev ca-certificates && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel && pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["/bin/bash", "-c", "python -m pip list && python -u tests/case_1.py && python -u tests/case_2.py && python -u tests/case_3.py"]
