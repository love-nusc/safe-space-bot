FROM python:3.10

WORKDIR /python-bot

COPY . .

CMD ["python", "./src/test.py"]