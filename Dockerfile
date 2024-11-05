FROM python:3.12.7-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

ENV PYTHONPATH=/app

RUN apt-get update && apt-get install -y make
# COPY ./scripts /app/scripts

COPY ./app /app/app
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Sync the project
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--reload"]
