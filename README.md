# 596-S22-Backend
Backend Repo for 596RL Spring 2022

This repo uses Docker to containerize any processes used. In order to the run the repo, it is advised that you install docker. 

From there, all you need to do to run the container is:
```
docker build -t rescue:latest .
docker run --name rescue -p 5057:5057 --rm rescue:latest
```