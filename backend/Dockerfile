# Dockerfile

# official python image
FROM python:3.11

# set work directory
WORKDIR /backend-image

# copy source root
COPY . /backend-image

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /backend-image/requirements.txt

# starting
CMD ["python", "start.py"]
