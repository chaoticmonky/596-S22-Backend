import typing
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
import json


@strawberry.type
class User:
    id: int
    name: str
    age: int

def get_users():
    user_list = None
    with open("./users.json") as users:
        user_list = json.load(users)
    return user_list

@strawberry.type
class Query:
    users: typing.List(User) = strawberry.field(resolver=get_users)


schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)