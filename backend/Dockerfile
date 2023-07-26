FROM python:3.11

WORKDIR /backend-image

COPY . .

RUN pip install --no-cache-dir --upgrade -r /backend-image/requirements.txt

CMD ["python", "start.py"]
