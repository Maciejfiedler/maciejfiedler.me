FROM python:3.8.6-alpine3.12

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV HOST 0.0.0.0

EXPOSE 5000

# Dev

# CMD [ "python", "-m", "flask", "run" ]

# Prod

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "setup:app" ]