from core.GraphQLColumn import GraphQLColumn
from core.GraphQLForeignKey import GraphQLForeignKey
from utils.string_util import to_camel_case
from static.config import METADATA_TABLE


class GraphQLTable:
    """
    Encapsulates a GraphQL Table containing a list of columns of type GraphQLColumn
    All the heavy lifting for GraphQL generation is done using the data encapsulated in the GraphQLTable.
    """

    def __init__(
            self,
            table_name: str,
            columns: [GraphQLColumn],
            primary_key_fields: [str] = None,
            foreign_key: GraphQLForeignKey = None
    ):
        self.table_name = table_name
        self.primary_key_fields = primary_key_fields
        self.columns = columns
        self.foreign_key = foreign_key
        self.columnDicts = [{k: v for (k, v) in col.__dict__.items()} for col in self.columns]
        if foreign_key and isinstance(foreign_key.__dict__, dict):
            self.foreignKeyDicts = {k: v for (k, v) in foreign_key.__dict__.items()}
        else:
            self.foreignKeyDicts = None
        self.__populate_graph_ql_structs()

    def __populate_graph_ql_structs(self):
        self.db_model_name = to_camel_case(self.table_name, init_caps=True)
        self.graph_ql_model_name = self.db_model_name + "Model"
        self.graph_ql_query_alias = self.db_model_name.lower() + "s"

    @staticmethod
    def from_json(json_data: dict):
        """
        public static factory method that returns an instance of GraphQLTable given a metadata JSON
        """
        assert METADATA_TABLE(json_data)
        # assert "table_name" in json_data
        # assert "columns" in json_data and isinstance(json_data["columns"], list)

        _graph_ql_columns = [GraphQLColumn(**col) for col in json_data["columns"]]

        _table_data = {
            "table_name": json_data["table_name"],
            "columns": _graph_ql_columns,
            "primary_key_fields": json_data["primary_key_fields"]
        }

        if "foreign_key" in json_data and isinstance(json_data["foreign_key"], dict):
            _table_data["foreign_key"] = GraphQLForeignKey(**json_data["foreign_key"])

        return GraphQLTable(**_table_data)
