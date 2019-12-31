from utils.string_util import to_camel_case
from static.config import DB_FIELD_TYPE_MAP, COLUMN_QUERY_TYPES_MAP


class GraphQLColumn:
    """
    Encapsulates GraphQL column
    """
    def __init__(self, field_name: str, field_type: str, exclude_from_search: bool = False):
        self.field_name = field_name
        self.field_type = field_type
        self.exclude_from_search = exclude_from_search
        self.__populate_graph_ql_structs()

    def __populate_graph_ql_structs(self):

        self.db_field_type = DB_FIELD_TYPE_MAP.get(self.field_type)
        self.db_model_name = to_camel_case(self.field_name, init_caps=False)

        if self.exclude_from_search:
            self.query_types = None
        else:
            self.query_types = COLUMN_QUERY_TYPES_MAP.get(self.field_type)

