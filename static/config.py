import fastjsonschema

TEMPLATE_FOLDER = "template"

DB_MODELS_FOLDER = "database"
GRAPHQL_SCHEMA_FOLDER = "schema"
GRAPHQL_SERVER_FOLDER = "."

FILE_TYPES_MAP = {".tl": ".py"}

BLIND_COPY_FILES = [
    {"source_path": "template/database", "source_file": "__init__.py", "target": "{}/database"},
    {"source_path": "template/schema", "source_file": "__init__.py", "target": "{}/schema"},
    {"source_path": "template", "source_file": "requirements.txt", "target": "{}"}
]

BLIND_COPY_FOLDERS = [
    {"source": "template/db_utils", "target": "{}/db_utils"}
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

METADATA_TABLES = fastjsonschema.compile({"type": "array", "uniqueItems": True})

METADATA_TABLE = fastjsonschema.compile(
    {
        "type": "object",
        "required": ["table_name", "columns", "primary_key_fields"],
        "properties": {
            "table_name": {"type": "string"},
            "columns": {
                "type": "array",
                "uniqueItems": True,
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
                "uniqueItems": True,
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
                                "items": [{"type": "string"}], "minItems": 1, "uniqueItems": True
                            },
                            "parent_columns":
                                {
                                    "type": "array",
                                    "items": [{"type": "string"}], "minItems": 1, "uniqueItems": True
                                },
                        }
                    }
                ]
            }
        }
    }
)
