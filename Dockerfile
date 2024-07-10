FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}

RUN chmod +x ./scripts/entrypoint.sh

# Punto di ingresso per il container
ENTRYPOINT ["./scripts/entrypoint.sh"]