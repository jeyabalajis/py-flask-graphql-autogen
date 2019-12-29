from core.GraphQLColumn import GraphQLColumn


class TestGraphQLColumn:
    def test_graph_ql_column_object(self):
        _data = {"field_type": "str", "field_name": "contract_ref_number"}
        _graph_ql_column = GraphQLColumn(**_data)

        for key, value in _graph_ql_column.__dict__.items():
            if key == "field_name":
                assert value == "contract_ref_number"
            if key == "db_field_type":
                assert value == "String"
