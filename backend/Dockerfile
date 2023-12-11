# Dockerfile

FROM python:3.11 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

# exporting pypoetry dependencies as requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

# set work directory
WORKDIR /code

# install dependencies
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy source root
COPY characters_analyzer /code/app

# starting
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
