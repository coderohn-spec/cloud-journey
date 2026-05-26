FROM python:3.11-slim

WORKDIR /app

COPY day5.py .

RUN pip install requests

CMD ["python", "day5.py"]