from core.GraphQLColumn import GraphQLColumn
from core.GraphQLTable import GraphQLTable


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

    def test_graph_ql_table_from_json(self):
        _table_json = {
            "table_name": "contract_header",
            "columns": [
                {"field_type": "str", "field_name": "contract_ref_number"},
                {"field_type": "str", "field_name": "inco_term"},
            ]
        }

        _graph_ql_table = GraphQLTable.from_json(_table_json)

        assert len(_graph_ql_table.columns) == len(_table_json["columns"])

        print(_graph_ql_table.__dict__)


my_test = TestGraphQLTable()
my_test.test_graph_ql_table_from_json()
