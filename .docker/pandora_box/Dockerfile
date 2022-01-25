FROM python:3.9-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install -y -- \
    gettext \
    git \
    build-essential \
    libpq-dev

COPY ./pandora_box/requirements/base.txt requirements/base.txt
COPY ./pandora_box/requirements.txt . 
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY ./pandora_box .
COPY ./pandora_box/app.py .

ENV PORT=5000
EXPOSE 5000

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 10 pandora_box.app:app