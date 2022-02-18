FROM python:3.9

WORKDIR /backend

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./app /backend/app