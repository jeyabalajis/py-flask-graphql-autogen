TEMPLATE_FOLDER = "template"

DB_MODELS_FOLDER = "database"

GRAPHQL_SCHEMA_FOLDER = "graphql"

FILE_TYPES_MAP = {".tl": ".py"}

BLIND_COPY_FILES = [
    "database/__init__.py",
    "graphql/__init__.py",
    "requirements.txt"
]

BLIND_COPY_FOLDERS = [
    "db_utils"
]

DB_FIELD_TYPE_MAP = {
    "str": "String",
    "int": "Integer",
    "date": "Date",
    "datetime": "DateTime"
}


COLUMN_QUERY_TYPES_MAP = {
    "str": [
        {"q_type": "in", "gql_type": "graphene.List(graphene.String)"},
        {"q_type": "like", "gql_type": "graphene.String()"},
        {"q_type": "eq", "gql_type": "graphene.String()"},
        {"q_type": "neq", "gql_type": "graphene.String()"}
    ],
    "int": [
        {"q_type": "gte", "gql_type": "graphene.Int()"},
        {"q_type": "lte", "gql_type": "graphene.Int()"},
        {"q_type": "gt", "gql_type": "graphene.Int()"},
        {"q_type": "lt", "gql_type": "graphene.Int()"},
    ],
    "date": [
        {"q_type": "gte", "gql_type": "graphene.Date()"},
        {"q_type": "lte", "gql_type": "graphene.Date()"},
        {"q_type": "gt", "gql_type": "graphene.Date()"},
        {"q_type": "lt", "gql_type": "graphene.Date()"},
    ],
    "datetime": [
        {"q_type": "gte", "gql_type": "graphene.DateTime()"},
        {"q_type": "lte", "gql_type": "graphene.DateTime()"},
        {"q_type": "gt", "gql_type": "graphene.DateTime()"},
        {"q_type": "lt", "gql_type": "graphene.DateTime()"},
    ]
}
