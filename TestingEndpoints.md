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

## Add Post
* Mutations
```
mutation addPost {
  addPost(postData: {
    userId: 1,
    title: "My first Post",
    body: "This is a Post about myself"
  })
  {
    id
  }
}
```

* Response
```
{
  "data": {
    "addPost": {
      "id": 1
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

## Add Comment
* Mutations
```
mutation createComment {
  addComment(commentData: {
    userId: 1,
    postId: 1,
    body: "Another Comment"
  })
  {
    id
    body
  }
}
```

* Response
```

```

* Exceptions on running the same mutation twice
```

```

## Get Users
* Query
```
query getAllUsers {
  users{
    id
    name
    posts {
      title
    }
  }
}
```

* Response
```
{
  "data": {
    "users": [
      {
        "id": 1,
        "name": "John Doe",
        "posts": [
          {
            "title": "My first Post"
          }
        ]
      }
    ]
  }
}
```

* Exceptions on running the same mutation twice
```

```

## Get Single Users
* Query
```
query getUser {
  getSingleUser(userId: 1) {
    name
    posts {
      title
      comments {
        body
      }
    }
    comments {
      body
    }
  }
}
```

* Response
```
{
  "data": {
    "getSingleUser": {
      "name": "John Doe",
      "posts": [
        {
          "title": "My first Post",
          "comments": [
            {
              "body": "Another Comment"
            }
          ]
        }
      ],
      "comments": [
        {
          "body": "Another Comment"
        }
      ]
    }
  }
}
```

* Exceptions on running the same mutation twice
```

```