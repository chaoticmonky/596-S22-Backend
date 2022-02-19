# 596-S22-Backend
Backend Repo for 596RL Spring 2022

.
├── app
│   ├── __init__.py
│   └── main.py
│   └── models.py
│   └── schemas.py
│   └── database.py
│   └── crud.py
├── Alembic
├── Dockerfile
└── requirements.txt

~~ MUST BE INSTALLED ~~
- Docker

This repo uses Docker to containerize any processes used. In order to the run the repo, it is advised that you install docker.

Make sure the Docker and the postgresSQL library are working.

From there, all you need to do to run the container is:
```
docker-compose up -d --build
docker-compose up
```
