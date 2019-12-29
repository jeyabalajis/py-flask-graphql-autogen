# py-flask-graphql-autogen

A tool that automatically generates GraphQL Server along with GraphQL types, resolvers and SQLAlchemy models for database tables!

- Supports all sensible search criteria on database columns
- Supports search on multiple columns
- Uses [jinja2](https://jinja.palletsprojects.com/en/2.10.x/) template engine for code generation
- Database engine can be plugged in post code generation in an isolated code file that __does not__ touch auto generated code 

## Features

- v1.0
    - Query resolvers with sensible search criteria for fields based on field types
