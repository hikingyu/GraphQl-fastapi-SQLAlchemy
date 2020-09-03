#!/usr/bin/env python
from schema import schema

from fastapi import FastAPI
from starlette.graphql import GraphQLApp

example_query = """
{
  allEmployees(sort: [NAME_ASC, ID_ASC]) {
    edges {
      node {
        id
        name
        department {
          id
          name
        }
        role {
          id
          name
        }
      }
    }
  }
}
"""

app = FastAPI()
app.add_route("/", GraphQLApp(schema=schema,graphiql=True))

if __name__ == "__main__":
    from database import init_db
    import uvicorn
    init_db()    
    uvicorn.run(app,port=5000,debug=True)