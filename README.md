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

### MUST BE INSTALLED
- Docker

This repo uses Docker to containerize any processes used. In order to the run the repo, it is advised that you install docker.

Make sure the Docker and the postgresSQL library are working.

From there, all you need to do to run the container is:
```
docker-compose up -d --build
docker-compose up
```

### Configuring PostgreSQL Server with Alembic
In order to begin posting to routes and adding in data, you will need to load in all the proper tables. Using Alembic this is really easy.

First, initialize your alembic configuration:
```
alembic init alembic
```

Next, you need to upgrade the head in order to setup all the tables properly:
```
alembic upgrade head
```

### Downgrading and Upgrading the Database
Using alembic, you can downgrade to a previous version by typing:
```
alembic downgrade -1
```

Or you can upgrade 1 version by typing:
```
alembic upgrade +1
```
