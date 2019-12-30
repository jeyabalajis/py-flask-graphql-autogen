from utils.string_util import to_camel_case


class GraphQLForeignKey:
    def __init__(self, parent_table_name: str, self_columns: [str], parent_columns: [str]):
        self.parent_table_name = parent_table_name
        self.self_columns = self_columns
        self.parent_columns = parent_columns
        self.parent_db_model_name = to_camel_case(parent_table_name, init_caps=True)
