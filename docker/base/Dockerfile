FROM python:3.9.7-slim

ENV PYTHONPATH "${PYTHONPATH}:/srv:/srv/src"

WORKDIR /srv

COPY pyproject.toml /srv/pyproject.toml
COPY poetry.lock /srv/poetry.lock
COPY setup.cfg /srv/setup.cfg

RUN python -m venv /srv

RUN pip install poetry && \
    POETRY_VIRTUALENVS_CREATE=false poetry install --no-ansi

RUN useradd -d /srv mowers \
    && chown mowers:mowers /srv
