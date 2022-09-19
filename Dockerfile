FROM python:3.9 as python-base

# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=1.2.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv

# Tell Poetry where to place its cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache

# Create stage for Poetry installation
FROM python-base as poetry-base

# Creating a virtual environment just for poetry and install it with pip
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Create a new stage from the base python image
FROM python-base as example-app

# Copy Poetry to app image
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Install dependencies
# set work directory
WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml README.md ./

RUN poetry check

RUN mkdir t5_fastapi
RUN mkdir schemes
RUN mkdir core
RUN mkdir api
COPY ./schemes/translateSchemas.py ./schemes/
COPY ./t5_fastapi/main.py ./t5_fastapi/
COPY ./core/config.py ./core/
WORKDIR /usr/src/app/api
RUN mkdir v1
WORKDIR /usr/src/app
COPY ./api/v1/translate.py ./api/v1/
RUN poetry install --no-interaction --no-ansi --no-cache
EXPOSE 8000
CMD [ "poetry", "run", "start"]