from sqlalchemy import *
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
    )
from sqlalchemy.ext.declarative import declarative_base
from db_utils.db_session_maker import get_db_session


db_session = get_db_session()

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()



{%- for table in data.tables %}

class {{table.db_model_name}}(Base):
    __tablename__ = '{{table.table_name}}'
    {% for col in table.columnDicts -%}
    {{col.field_name}} = Column({{col.db_field_type}})
    {% endfor %}

    {%- if (table.foreignKeyDicts is not none and table.foreignKeyDicts is iterable) %}
    {{table.foreignKeyDicts.parent_db_model_name.lower()}} = relationship(
        {{table.foreignKeyDicts.parent_db_model_name}},
        backref=backref('{{table.db_model_name.lower()}}',
                        uselist=True,
                        cascade='delete,all'))
    {%- endif %}

    {% if (table.primary_key_fields is not none and table.primary_key_fields is iterable)%}
    __table_args__ = (
        PrimaryKeyConstraint(
        {%- for field in table.primary_key_fields -%}
            '{{field}}' {%- if not loop.last %},{%endif -%}
        {% endfor %}),
        {%- if (table.foreignKeyDicts is not none and table.foreignKeyDicts is iterable) %}
        ForeignKeyConstraint(
            ({%- for col in table.foreignKeyDicts.self_columns -%}{{col}},{% endfor %}),
            [{%- for col in table.foreignKeyDicts.parent_columns -%}
            {{table.foreignKeyDicts.parent_db_model_name}}.{{col}}
            {%- if not loop.last %},{%endif -%} {% endfor %}]
        ),
        {%- endif %}
        {},
    )
    {% endif %}

{% endfor %}
