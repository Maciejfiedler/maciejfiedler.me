FROM python:3.8.6-alpine3.12

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#Dev
RUN export FLASK_APP=app
RUN export FLASK_ENV=development
CMD [ "python", "-m", "flask", "run" ]