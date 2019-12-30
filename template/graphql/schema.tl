import graphene
from graphene import relay, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType

from {{data.db_models_folder}}.models import (
    {%- for table in data.tables %}
    {{table.db_model_name}} as {{table.graph_ql_model_name}}{%- if not loop.last %},{%endif -%}
    {% endfor %}
)

{# Loop through tables and #}
{%- for table in data.tables %}
class {{table.db_model_name}}(SQLAlchemyObjectType):
    class Meta:
        model = {{table.graph_ql_model_name}}
        interfaces = (relay.Node,)

{% endfor %}

class Query(ObjectType):
    node = relay.Node.Field()
    params = dict(limit=graphene.Int(), offset=graphene.Int())
    {# Generate query all variables #}
    {%- for table in data.tables %}
    all_{{table.graph_ql_query_alias}} = graphene.List(lambda: {{table.db_model_name}}, **params)
    {% endfor %}

    {# Generate query all resolvers #}
    {%- for table in data.tables %}
    def resolve_all_{{table.graph_ql_query_alias}}(self, info, **args):
        limit = args.get("limit")
        offset = args.get("offset")
        {{table.db_model_name.lower()}}_query = {{table.db_model_name}}.get_query(info)

        {{table.graph_ql_query_alias}} = {{table.db_model_name.lower()}}_query.filter().limit(limit)

        return {{table.graph_ql_query_alias}}
    {% endfor %}

    find_employee_by_name = graphene.List(lambda: Employee, name=graphene.String())

    def resolve_find_employee_by_name(self, info, **args):
        name = args.get("name")
        employee_query = Employee.get_query(info)

        employees = employee_query.filter(EmployeeModel.name.contains(name)).all()

        return employees


schema = graphene.Schema(query=Query)
