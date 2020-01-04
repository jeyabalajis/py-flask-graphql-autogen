import pytest
from fastjsonschema.exceptions import JsonSchemaException

from core.GraphQLColumn import GraphQLColumn
from core.GraphQLForeignKey import GraphQLForeignKey
from core.GraphQLTable import GraphQLTable
from static.config import METADATA_TABLE


class TestGraphQLTable:
    def test_graph_ql_table_object(self):
        _col_data = [
            {"field_type": "str", "field_name": "contract_ref_number"},
            {"field_type": "str", "field_name": "inco_term"},
        ]

        _graph_ql_columns = [GraphQLColumn(**col) for col in _col_data]

        _table_data = {"table_name": "contract_header", "columns": _graph_ql_columns}
        _graph_ql_table = GraphQLTable(**_table_data)

        assert len(_graph_ql_table.columns) == len(_col_data)

    def test_foreign_key(self):
        _col_data = [
            {"field_type": "str", "field_name": "contract_ref_number"},
            {"field_type": "str", "field_name": "inco_term"},
        ]

        _graph_ql_columns = [GraphQLColumn(**col) for col in _col_data]

        _table_data = {"table_name": "contract_header", "columns": _graph_ql_columns}
        _graph_ql_table = GraphQLTable(**_table_data)

        assert _graph_ql_table.foreignKeyDicts is None

        _foreign_key_data = {
            "parent_table_name": "department",
            "self_columns": ["department_id"],
            "parent_columns": ["id"]
        }
        _foreign_key = [GraphQLForeignKey(**_foreign_key_data)]

        _table_data = {"table_name": "contract_header", "columns": _graph_ql_columns, "foreign_key_fields": _foreign_key}
        _graph_ql_table = GraphQLTable(**_table_data)

        assert _graph_ql_table.foreignKeyDicts is not None

    def test_graph_ql_table_from_json(self):
        _table_json = {
            "table_name": "contract_header",
            "columns": [
                {"field_type": "str", "field_name": "contract_ref_number"},
                {"field_type": "str", "field_name": "inco_term"},
            ],
            "primary_key_fields": ["contract_ref_number"]
        }

        _graph_ql_table = GraphQLTable.from_json(_table_json)

        assert len(_graph_ql_table.columns) == len(_table_json["columns"])

        print(_graph_ql_table.__dict__)

    def test_metadata_json(self):
        _table_json_invalid = {}
        with pytest.raises(JsonSchemaException):
            assert METADATA_TABLE(_table_json_invalid)
