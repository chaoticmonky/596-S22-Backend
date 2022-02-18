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
- PostgreSQL

This repo uses Docker to containerize any processes used. In order to the run the repo, it is advised that you install docker. 

From there, all you need to do to run the container is:
```
docker build -t rescue:latest .
docker run --name rescue -p 80:80 --rm rescue:latest
```