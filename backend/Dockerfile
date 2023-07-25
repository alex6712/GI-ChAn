# Dockerfile

# official python image
FROM python:3.11

# set work directory
WORKDIR /backend

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy source root
COPY . .
