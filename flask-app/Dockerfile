FROM python:3.10.12-alpine3.17

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0" ]