# Dockerfile

# official python image
FROM python:3.11

# set work directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy source root
COPY ./app /code

# starting
CMD ["python", "start.py"]
