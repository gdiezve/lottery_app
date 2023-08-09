FROM python:3.8.6-buster
LABEL authors="georginadiez"

RUN apt update
RUN apt-get install cron -y && apt install postgresql postgresql-contrib -y
RUN alias py=python

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

# django-crontab logfile
RUN mkdir /cron && touch /cron/django_cron.log

EXPOSE 8000

CMD service cron start &&  python3 manage.py crontab add && python3 manage.py migrate && psql -h db -d lottery -a -f sql/fill_tables.sql && python3 manage.py runserver 0.0.0.0:8000