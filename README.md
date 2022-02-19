# 596-S22-Backend
Backend Repo for 596RL Spring 2022

.                                       \n
├── app                                 \n
│   ├── __init__.py                     \n
│   └── main.py                         \n
│   └── models.py                       \n
│   └── schemas.py                      \n
│   └── database.py                     \n
│   └── crud.py                         \n
├── Alembic                             \n
├── Dockerfile                          \n
└── requirements.txt                    \n

~~ MUST BE INSTALLED ~~
- Docker

This repo uses Docker to containerize any processes used. In order to the run the repo, it is advised that you install docker.

Make sure the Docker and the postgresSQL library are working.

From there, all you need to do to run the container is:
```
docker-compose up -d --build
docker-compose up
```