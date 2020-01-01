# py-flask-graphql-autogen

A tool that __automatically generates deploy ready GraphQL Server__ based on database table metadata. 

## Why?
The motivation for this tool is two-fold:
1. Building API end points for simple database models is a chore. This tool will automate the whole process.
2. If you have a data warehouse (DWH) which you want to expose to external systems as a _Data API_, this tool will come in handy. 

## Salient Features
- Supports all sensible search criteria on database columns based on field types
- Supports search on a combination of columns
- Ability to plug in database connection parameters without disturbing auto-generated code 
- Uses [jinja2](https://jinja.palletsprojects.com/en/2.10.x/) template engine for [PEP8](https://www.python.org/dev/peps/pep-0008/) compliant code generation.

## Releases

### v1.0
- Query resolvers with sensible search criteria for fields based on field types
    - __String__:
        1. ilike search (i.e. case insensitive like search)
        2. starts with, ends with search
        3. in list search
        4. equals, not equals search
    - __Numeric__:
        1. greater than, less than
        2. between
        3. equals, not equals
    - __Date__:
        1. greater than, less than
        2. between
        3. equals, not equals        
- Combination search on fields, which provides a powerful API to model complex queries
- Ability to exclude specific columns from being part of the query
- REST API GET endpoint to send metadata json as an input and receive GraphQL Server project as an output (as a base64 encoded string) 
### Immediate Road map
- Provision for authentication and authorization
- Provision for caching