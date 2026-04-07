FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir numpy pillow openai

CMD ["python", "inference.py"]