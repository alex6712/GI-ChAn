FROM python:3.11

WORKDIR /code

RUN ls

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code

CMD ["python", "start.py"]
