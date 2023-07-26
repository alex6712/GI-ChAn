# Dockerfile

# official python image
FROM python:3.11

# set work directory
WORKDIR /backend-image

# install dependencies
COPY ./requirements.txt /backend-image
RUN pip install --no-cache-dir --upgrade -r /backend-image/requirements.txt

# copy source root
COPY ./ /backend-image

# starting
CMD ["python", "start.py"]
