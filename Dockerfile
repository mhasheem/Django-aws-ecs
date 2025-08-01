FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
COPY templates/ templates/

CMD [ "python3", "manage.py","runserver","0.0.0.0:8000" ]
