import graphene
from graphene import relay, ObjectType
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import and_
from {{data.db_models_folder}}.models import (
    {%- for table in data.tables %}
    {{table.db_model_name}} as {{table.graph_ql_model_name}}{%- if not loop.last %},{%endif -%}
    {% endfor %}
)

{# Macros START #}
{% macro add_to_filter(table, col, query_type) %}
        if {{col.db_model_name}}_{{query_type.q_type}}:
            {%- if query_type.q_type|upper == 'IN'  %}
            filter_criteria.append({{table.graph_ql_model_name}}.{{col.field_name}}.in_({{col.db_model_name}}_{{query_type.q_type}}))
            {%- endif  %}

            {%- if query_type.q_type|upper == 'LIKE'  %}
            filter_criteria.append({{table.graph_ql_model_name}}.{{col.field_name}}.contains({{col.db_model_name}}_{{query_type.q_type}}))
            {%- endif  %}

            {%- if query_type.q_type|upper == 'EQ'  %}
            filter_criteria.append({{table.graph_ql_model_name}}.{{col.field_name}} == {{col.db_model_name}}_{{query_type.q_type}})
            {%- endif  %}

            {%- if query_type.q_type|upper == 'NEQ'  %}
            filter_criteria.append({{table.graph_ql_model_name}}.{{col.field_name}} != {{col.db_model_name}}_{{query_type.q_type}})
            {%- endif  %}

            {%- if query_type.q_type|upper == 'GTE'  %}
            filter_criteria.append({{table.graph_ql_model_name}}.{{col.field_name}} >= {{col.db_model_name}}_{{query_type.q_type}})
            {%- endif  %}

            {%- if query_type.q_type|upper == 'GT'  %}
            filter_criteria.append({{table.graph_ql_model_name}}.{{col.field_name}} > {{col.db_model_name}}_{{query_type.q_type}})
            {%- endif  %}

            {%- if query_type.q_type|upper == 'LTE'  %}
            filter_criteria.append({{table.graph_ql_model_name}}.{{col.field_name}} <= {{col.db_model_name}}_{{query_type.q_type}})
            {%- endif  %}

            {%- if query_type.q_type|upper == 'LT'  %}
            filter_criteria.append({{table.graph_ql_model_name}}.{{col.field_name}} < {{col.db_model_name}}_{{query_type.q_type}})
            {%- endif  %}
{% endmacro %}
{# Macros END #}

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

    {%- for table in data.tables %}
    {# Generate multi - field search query parameters #}
    query_params_dict = dict()
    {% for col in table.columnDicts -%}
    {%- if (col.query_types is not none and col.query_types is iterable) %}
    {% for query_type in col.query_types -%}
    query_params_dict['{{col.db_model_name}}_{{query_type.q_type}}'] = {{query_type.gql_type}}
    {% endfor %} {# end of query types loop #}
    {% endif %} {# end of query_types iterable condition #}
    {% endfor %} {# end of columns loop #}

    query_params_dict['limit'] = graphene.Int()
    search_{{table.graph_ql_query_alias}} = graphene.List(lambda: {{table.db_model_name}}, **query_params_dict)

    def resolve_search_{{table.graph_ql_query_alias}}(self, info, **args):

        {# Initialize the filter criteria #}
        filter_criteria = []

        {% for col in table.columnDicts -%}
        {%- if (col.query_types is not none and col.query_types is iterable) %}
        {% for query_type in col.query_types -%}
        {{col.db_model_name}}_{{query_type.q_type}} = args.get("{{col.db_model_name}}_{{query_type.q_type}}")

        {{ add_to_filter(table, col, query_type) }}

        {% endfor %} {# end of query types loop #}
        {% endif %} {# end of query_types iterable condition #}
        {% endfor %} {# end of columns loop #}

        limit = args.get("limit")

        filter_rule = and_(*filter_criteria)

        {{table.db_model_name.lower()}}_query = {{table.db_model_name}}.get_query(info)

        {{table.graph_ql_query_alias}} = {{table.db_model_name.lower()}}_query.filter(filter_rule).limit(limit)

        return {{table.graph_ql_query_alias}}

    {% endfor %} {# end of tables loop #}

schema = graphene.Schema(query=Query)
