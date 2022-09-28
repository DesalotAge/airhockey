FROM python:3.10.4
ENV PYTHONUNBUFFERED 1


RUN apt-get update &&\
    pip install --upgrade pip &&\
    pip install poetry &&\
    poetry config virtualenvs.create false

WORKDIR /app

COPY ./backend/poetry.lock  /app
COPY ./backend/pyproject.toml /app

RUN poetry install

COPY ./backend/airhockey_backend /app

EXPOSE 8080

CMD python main.py
