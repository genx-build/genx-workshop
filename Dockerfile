FROM python:3.11-slim

COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
CMD ["bash", "run.sh"]