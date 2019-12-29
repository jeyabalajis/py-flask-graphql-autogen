from core.GraphQLColumn import GraphQLColumn


class GraphQLTable:
    """
    Encapsulates a GraphQL Table containing a list of columns of type GraphQLColumn
    All the heavy lifting for GraphQL generation is done using the data encapsulated in the GraphQLTable.
    """

    def __init__(self, table_name: str, columns: [GraphQLColumn], primary_key_fields: [str]=None):
        self.table_name = table_name
        self.primary_key_fields = primary_key_fields
        self.columns = columns
        self.columnDicts = [{k: v for (k, v) in col.__dict__.items()} for col in self.columns]

    @staticmethod
    def from_json(json_data):
        assert "table_name" in json_data
        assert "columns" in json_data and isinstance(json_data["columns"], list)

        _graph_ql_columns = [GraphQLColumn(**col) for col in json_data["columns"]]

        _table_data = {"table_name": json_data["table_name"], "columns": _graph_ql_columns}
        return GraphQLTable(**_table_data)

    def process_db_models(self):
        pass


class GraphQLTblSqlAlchemy(GraphQLTable):
    """
    SqlAlchemy flavor of GraphQL Table. Used to generate SQL Alchemy models
    """
    def generate_dao_models(self):
        pass
