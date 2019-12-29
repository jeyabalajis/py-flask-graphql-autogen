class GraphQLColumn:
    """
    Encapsulates GraphQL column
    """
    def __init__(self, field_name: str, field_type: str):
        self.field_name = field_name
        self.field_type = field_type
        self.__populate_template_fields()

    def __populate_template_fields(self):
        db_field_type_map = {
            "str": "String",
            "int": "Integer",
            "date": "Date",
            "datetime": "DateTime"
        }
        self.db_field_type = db_field_type_map.get(self.field_type)
