from utils.template_util import render_template
from core.GraphQLTable import GraphQLTable
from core.GraphQLColumn import GraphQLColumn
from core.GraphQLForeignKey import GraphQLForeignKey


class TestTemplateUtil:
    def test_render_template(self):
        tables = []
        _col_data = [
            {"field_type": "int", "field_name": "id"},
            {"field_type": "str", "field_name": "name"}
        ]
        _graph_ql_columns = [GraphQLColumn(**col) for col in _col_data]

        _table_data = {
            "table_name": "department",
            "columns": _graph_ql_columns,
            "primary_key_fields": ["id"]
        }
        _graph_ql_table = GraphQLTable(**_table_data)

        tables.append(_graph_ql_table.__dict__)

        _col_data = [
            {"field_type": "int", "field_name": "id"},
            {"field_type": "str", "field_name": "name"},
            {"field_type": "datetime", "field_name": "hired_on"},
            {"field_type": "int", "field_name": "department_id"}
        ]

        _graph_ql_columns = [GraphQLColumn(**col) for col in _col_data]

        _foreign_key_data = {
            "parent_table_name": "department",
            "self_columns": ["department_id"],
            "parent_columns": ["id"]
        }
        _foreign_key = GraphQLForeignKey(**_foreign_key_data)

        _table_data = {
            "table_name": "employee",
            "columns": _graph_ql_columns,
            "primary_key_fields": ["id"],
            "foreign_key": _foreign_key
        }
        _graph_ql_table = GraphQLTable(**_table_data)

        tables.append(_graph_ql_table.__dict__)

        data = {
            "tables": tables
        }

        output = render_template("models", "models.tl", data)
        print(output)
        assert output.find("PrimaryKeyConstraint") is not None


my_test = TestTemplateUtil()
my_test.test_render_template()