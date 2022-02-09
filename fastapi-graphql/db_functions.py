from schemas import User
import json

def get_users():
    return [
        User(
            id=1,
            name="Jagath Jai Kumar",
            age=207
        ),
        User(
            id=2,
            name="Benjamin Glickenhaus",
            age=208
        ),
        User(
            id=3,
            name="Sam DuBois",
            age=21
        ),
        User(
            id=4,
            name="Andres Gutierrez",
            age=22
        ),
    ]