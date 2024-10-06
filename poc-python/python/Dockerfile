FROM python:3.12-alpine

COPY ./app /var/local/app

RUN pip install -r /var/local/app/requirements.txt

EXPOSE 8080

CMD ["python", "/var/local/app/app.py"]