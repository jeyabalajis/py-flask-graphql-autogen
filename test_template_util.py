from utils.TemplateUtil import TemplateUtil
from core.GraphQLTable import GraphQLTable
from core.GraphQLColumn import GraphQLColumn
from core.GraphQLForeignKey import GraphQLForeignKey
from static.config import DB_MODELS_FOLDER, GRAPHQL_SCHEMA_FOLDER
from os import path


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
            {"field_type": "int", "field_name": "department_id", "exclude_from_search": True}
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

        print(_graph_ql_table.__dict__)
        tables.append(_graph_ql_table.__dict__)

        data = {
            "db_models_folder": DB_MODELS_FOLDER,
            "tables": tables
        }

        template_util = TemplateUtil(DB_MODELS_FOLDER, "models.tl", data)
        template_util.render_template_to_file("out/" + DB_MODELS_FOLDER, "models.tl".replace(".tl", ".py"))
        assert path.exists("out/" + DB_MODELS_FOLDER + "/" + "models.py")

        template_util = TemplateUtil(GRAPHQL_SCHEMA_FOLDER, "schema.tl", data)
        template_util.render_template_to_file("out/" + GRAPHQL_SCHEMA_FOLDER, "schema.tl".replace(".tl", ".py"))
        assert path.exists("out/" + GRAPHQL_SCHEMA_FOLDER + "/" + "schema.py")
