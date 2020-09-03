# FastApi & Graphene-SQLAlchemy(GraphQL) Example
This is an example project for using GraphQL with Flask using Graphene-SQLAlchemy.
## Running  Server
```
python app.py
```
## Creating a new Database
Create a database(Used SQLite) with the table structure mentioned in struct.sql and update the database name in database.py file.
```
database.py

# Replace 'sqlite:///rfg.db' with your path to database

engine = create_engine('sqlite:///rfg.db', convert_unicode=True)
```
## Testing GraphQL
Go to http://localhost:5000/graphql to try GraphQL. Below are the example queries for adding a new user, getting all users, searching for a user with username and updating username with email id.
## Adding a New User
```
mutation {
  createUser(name: "abc", email: "hello@abc.com", username: "abc") {
    user {
      id,
      name,
      email,
      username
    }
    ok
  }
}
```
Getting All Users List
```
{
  allUsers {
    edges {
      node {
        name,
        email,
        username
      }
    }
  }
}
```
## Finding a User with Username
```
{
  findUser(username: "rahulmfg") {
    id,
    name,
    email
  }
}
```
## Updating Username With Email ID
```
mutation {
  changeUsername(email: "abc@abc.com", username:"newabc") {
    user {
      name,
      email,
      username
    }
  }
}
```
