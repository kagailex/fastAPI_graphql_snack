from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from core import Mutation

app = FastAPI()


@app.get("/")
def ping():
    return {"ping": "pong"}


@strawberry.type
class Query:
  @strawberry.field
  def hello(self) -> str:
    return "Hello World"

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")