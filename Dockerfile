FROM python:3.10

WORKDIR /python-bot

RUN pip install python-telegram-bot==13.8.1

COPY . .

CMD ["python", "./src/main.py"]