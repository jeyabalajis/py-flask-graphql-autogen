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


[![CircleCI](https://circleci.com/gh/jeyabalajis/py-flask-graphql-autogen.svg?style=svg)](https://circleci.com/gh/jeyabalajis/py-flask-graphql-autogen)

![](coverage.svg)

## Solution Approach
- The [template folder](./template) contains a representation of the target GraphQL API server
- The tool takes in table metadata json (for one or many tables) and app name as inputs
- The tool uses jinja2 template to inject table metadata json onto the template files under the template folder and generate target .py code files
- The tool uses [black](https://black.readthedocs.io/en/stable/) to format the code files generated    

## Releases

### v1.0
- Query resolvers that enables a combination __and__ search on  a multitude of fields, which provides a powerful API to model complex queries
- The query fields are automatically created based on field types
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
- Ability to exclude specific columns from being part of the query
- REST API GET endpoint to send metadata json as an input and receive GraphQL Server project as an output (as a base64 encoded string) 

### Immediate Road map
- Provision for authentication and authorization
- Provision for caching

## metadata json schema
```json
{
        "type": "object",
        "required": ["table_name", "columns", "primary_key_fields"],
        "properties": {
            "table_name": {"type": "string"},
            "columns": {
                "type": "array",
                "uniqueItems": true,
                "items": [
                    {
                        "type": "object",
                        "required": ["field_name", "field_type"],
                        "properties": {
                            "field_name": {"type": "string"},
                            "field_type": {"type": "string"},
                            "exclude_from_search": {"type": "boolean"}
                        }
                    }
                ],
                "minItems": 1
            },
            "primary_key_fields": {
                "type": "array",
                "uniqueItems": true,
                "items": [
                    {"type": "string"}
                ],
                "minItems": 1
            },
            "foreign_key_fields": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "required": ["parent_table_name", "self_columns", "parent_columns"],
                        "properties": {
                            "parent_table_name": {"type": "string"},
                            "self_columns": {
                                "type": "array",
                                "items": [{"type": "string"}], "minItems": 1, "uniqueItems": true
                            },
                            "parent_columns":
                                {
                                    "type": "array",
                                    "items": [{"type": "string"}], "minItems": 1, "uniqueItems": true
                                }
                        }
                    }
                ]
            }
        }
    }
```
