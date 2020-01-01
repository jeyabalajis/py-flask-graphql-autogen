from unittest import TestCase
from core.GraphQLServer import GraphQLServer
import tempfile
import os


class TestGraphQLServer(TestCase):
    def test_generate_graphql_server(self):
        _table_metadata = [
            {
                "table_name": "department",
                "columns": [
                    {"field_type": "int", "field_name": "id"},
                    {"field_type": "str", "field_name": "name"}
                ],
                "primary_key_fields": ["id"]
            },
            {
                "table_name": "employee",
                "columns": [
                    {"field_type": "int", "field_name": "id"},
                    {"field_type": "str", "field_name": "name"},
                    {"field_type": "datetime", "field_name": "hired_on"},
                    {"field_type": "int", "field_name": "department_id", "exclude_from_search": True}
                ],
                "primary_key_fields": ["id"],
                "foreign_key": {
                    "parent_table_name": "department",
                    "self_columns": ["department_id"],
                    "parent_columns": ["id"]
                }
            }
        ]

        # base_path = tempfile.gettempdir()
        base_path = "E:/GraphQLPOC"
        root_folder_name = "auto-graphql-demo"

        graph_ql_server = GraphQLServer(
            app_name="autoGraphqlDemo",
            base_path=base_path,
            root_folder_name=root_folder_name,
            table_meta_data=_table_metadata
        )

        graph_ql_server.generate_graphql_server()

        for root, d_names, f_names in os.walk(base_path + "/" + root_folder_name):
            print(root, d_names, f_names)


test = TestGraphQLServer()
test.test_generate_graphql_server()
