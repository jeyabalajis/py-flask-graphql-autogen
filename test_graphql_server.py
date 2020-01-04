from unittest import TestCase
from core.GraphQLServer import GraphQLServer
import tempfile
import os


class TestGraphQLServer(TestCase):
    def test_generate_graphql_server(self):
        # _table_metadata = [
        #     {
        #         "table_name": "department",
        #         "columns": [
        #             {"field_type": "int", "field_name": "id"},
        #             {"field_type": "str", "field_name": "name"}
        #         ],
        #         "primary_key_fields": ["id"]
        #     },
        #     {
        #         "table_name": "employee",
        #         "columns": [
        #             {"field_type": "int", "field_name": "id"},
        #             {"field_type": "str", "field_name": "name"},
        #             {"field_type": "datetime", "field_name": "hired_on"},
        #             {"field_type": "int", "field_name": "department_id", "exclude_from_search": True}
        #         ],
        #         "primary_key_fields": ["id"],
        #         "foreign_key": {
        #             "parent_table_name": "department",
        #             "self_columns": ["department_id"],
        #             "parent_columns": ["id"]
        #         }
        #     }
        # ]
        _table_metadata = [
            {
                "table_name": "business_partner",
                "columns": [
                    {"field_name": "partner_id", "field_type": "int"},
                    {"field_name": "partner_name", "field_type": "str"},
                    {"field_name": "partner_type", "field_type": "str"}
                ],
                "primary_key_fields": ["partner_id"]
            },
            {
                "table_name": "commodity",
                "columns": [
                    {"field_name": "commodity_id", "field_type": "int"},
                    {"field_name": "commodity_code", "field_type": "str"},
                    {"field_name": "commodity_name", "field_type": "str"}
                ],
                "primary_key_fields": ["commodity_id"]
            },
            {
                "table_name": "inco_term",
                "columns": [
                    {"field_name": "inco_term_id", "field_type": "int"},
                    {"field_name": "inco_term_code", "field_type": "str"}
                ],
                "primary_key_fields": ["inco_term_id"]
            },
            {
                "table_name": "inco_term_language",
                "columns": [
                    {"field_name": "inco_term_id", "field_type": "int"},
                    {"field_name": "language_code", "field_type": "str"},
                    {"field_name": "inco_term_desc", "field_type": "str"}
                ],
                "primary_key_fields": ["inco_term_id", "language_code"],
                "foreign_key_fields": [
                    {
                        "parent_table_name": "inco_term",
                        "self_columns": ["inco_term_id"],
                        "parent_columns": ["inco_term_id"]
                    }
                ]
            },
            {
                "table_name": "contract_header",
                "columns": [
                    {"field_name": "contract_id", "field_type": "int"},
                    {"field_name": "contract_ref_no", "field_type": "str"},
                    {"field_name": "contract_type", "field_type": "str"},
                    {"field_name": "inco_term_id", "field_type": "str"},
                    {"field_name": "commodity_id", "field_type": "int"},
                    {"field_name": "partner_id", "field_type": "int"}
                ],
                "primary_key_fields": ["contract_id"],
                "foreign_key_fields": [
                    {
                        "parent_table_name": "business_partner",
                        "self_columns": ["partner_id"],
                        "parent_columns": ["partner_id"]
                    },
                    {
                        "parent_table_name": "commodity",
                        "self_columns": ["commodity_id"],
                        "parent_columns": ["commodity_id"]
                    },
                    {
                        "parent_table_name": "inco_term",
                        "self_columns": ["inco_term_id"],
                        "parent_columns": ["inco_term_id"]
                    }
                ]
            },
            {
                "table_name": "contract_line_item",
                "columns": [
                    {"field_name": "contract_id", "field_type": "int"},
                    {"field_name": "item_id", "field_type": "int"},
                    {"field_name": "delivery_start_date", "field_type": "date"},
                    {"field_name": "delivery_end_date", "field_type": "date"},
                    {"field_name": "open_quantity", "field_type": "int"},
                    {"field_name": "item_status", "field_type": "str"}
                ],
                "primary_key_fields": ["contract_id", "item_id"],
                "foreign_key_fields": [
                    {
                        "parent_table_name": "contract_header",
                        "self_columns": ["contract_id"],
                        "parent_columns": ["contract_id"]
                    }
                ]
            }
        ]

        # base_path = tempfile.gettempdir()
        base_path = "C:/Temp/GraphQLPOC"
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
