FROM python:3.9-slim
WORKDIR /app
COPY ./source_code /app
CMD ["python", "main.py"]