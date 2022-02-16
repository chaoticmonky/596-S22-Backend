FROM python:3.9-alpine

RUN adduser -D rescue

WORKDIR /home/rescue

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY __init__.py ./
COPY main.py ./
COPY crud.py ./
COPY models.py ./
COPY schemas.py ./
COPY database.py ./

RUN chown -R rescue:rescue ./
USER rescue

CMD uvicorn main:app --host 0.0.0.0 --port 5057