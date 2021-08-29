FROM python:alpine3.14

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["python","manage.py", "runserver","0.0.0.0:5000"]


