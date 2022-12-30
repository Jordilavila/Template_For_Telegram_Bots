FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY mkdocs.yml .
COPY /docs /docs
COPY mkdocs-requirements.txt .
RUN pip install -r mkdocs-requirements.txt
COPY /database /database
COPY /logs /logs
COPY /src /src
COPY my_telegram_bot.py .
COPY .env.example .env
#RUN python3 my_telegram_bot.py
