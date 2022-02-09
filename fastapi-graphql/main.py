from typing import List
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schemas import User
from db_functions import get_users

@strawberry.type
class Query:
    users: List[User] = strawberry.field(resolver=get_users)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)