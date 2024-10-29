# Testing Mutations
## Add User 
* Mutations
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

* Response
```
{
  "data": {
    "addUser": {
      "id": 1,
      "name": "John Doe",
      "address": "My home address"
    }
  }
}
```
* Exceptions on running the same mutation twice
```
{
  "data": null,
  "errors": [
    {
      "message": "User already exists",
      "locations": [
        {
          "line": 33,
          "column": 3
        }
      ],
      "path": [
        "addUser"
      ]
    }
  ]
}
```