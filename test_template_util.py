from utils.template_util import render_template
from core.GraphQLTable import GraphQLTable
from core.GraphQLColumn import GraphQLColumn


class TestTemplateUtil:
    def test_render_template(self):
        _col_data = [
            {"field_type": "str", "field_name": "contract_ref_number"},
            {"field_type": "str", "field_name": "inco_term"},
            {"field_type": "int", "field_name": "version"}
        ]

        _graph_ql_columns = [GraphQLColumn(**col) for col in _col_data]

        _table_data = {
            "table_name": "contract_header",
            "columns": _graph_ql_columns,
            "primary_key_fields": ["contract_ref_number"]
        }
        _graph_ql_table = GraphQLTable(**_table_data)

        output = render_template("models", "models.tl", _graph_ql_table.__dict__)
        print(output)
        assert output.find("PrimaryKeyConstraint") is not None


my_test = TestTemplateUtil()
my_test.test_render_template()