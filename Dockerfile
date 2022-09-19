FROM python:3.10

WORKDIR /python-bot

RUN pip install python-telegram-bot

COPY . .

CMD ["python", "./src/main.py"]