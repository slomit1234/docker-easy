FROM python:3.9-alpine

WORKDIR /app

COPY server.py .
COPY client.py .

CMD ["python", "server.py"]

