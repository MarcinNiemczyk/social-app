FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION 1.8.1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip3 install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY ./backend /code

RUN poetry install --no-interaction --no-ansi

ENTRYPOINT ["uvicorn"]
CMD ["src.main:app", "--host", "0.0.0.0","--port", "8000", "--reload"]
