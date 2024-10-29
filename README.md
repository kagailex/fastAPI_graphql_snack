# fastapi_graphql_snack
Demonstrate the usage of graphql and FastAPI.

## Tools used
* [FastAPI](https://fastapi.tiangolo.com/)
* [GraphQL Library (strawberry-graphql](https://strawberry.rocks/docs/integrations/fastapi)
* [Masonite ORM](https://orm.masoniteproject.com/)

## Setup projects
* Create virtual environment
```
python3 -m venv venv
```

* Activate virtual environment
```
source venv/bin/activate
```

* Install dependencies
```
pip install -r requirements.txt
```

* Run the database
```
docker compose up -d

docker compose down # To stop the database
```

## Running the project
* Running the code(DEV)
```
docker compose up -d
uvicorn main:app --reload
```

## View
* View the API DOCS [HERE](http://127.0.0.1:8000)
* View database UI [HERE](http://127.0.0.1:8080)


## Commands
### Create models
* masonite-orm model User --directory models - Creating the User model.
* masonite-orm model Post --directory models - Creating the Post model.
* masonite-orm model Comment --directory models - Creating the Comment model.

### Create the initial migrations
* masonite-orm migration migration_for_user_table --create users
* masonite-orm migration migration_for_post_table --create posts
* masonite-orm migration migration_for_comment_table --create comments

### Apply Migration
* masonite-orm migrate


## Testing
* Add user Mutation
```
mutation {
  addUser(userData:{
    name: "John Doe",
    email: "john@email.com",
    address: "My home address",
    phoneNumber: "1234567890",
    sex: "male"
  }){
    id
    name
    address
  }
}
```


## Credits
* [learning material](https://testdriven.io/blog/fastapi-graphql/)


## Additional resources / Notes
* [masoniteorm config/database.py](https://orm.masoniteproject.com/installation#configuration)
* [Schema & Migrations](https://orm.masoniteproject.com/schema-and-migrations)
* [Schema graphql](https://docs.graphene-python.org/en/latest/types/schema/)
* [Schema basics strawberry](https://strawberry.rocks/docs/general/schema-basics)
* [Mutations graphql](https://docs.graphene-python.org/en/latest/types/mutations/)

