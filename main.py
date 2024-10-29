from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from core import Mutation, Query

app = FastAPI()


@app.get("/")
def ping():
    return {"ping": "pong"}



schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")