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


class {{data.table_name}}(Base):
    __tablename__ = '{{data.table_name}}'
    {% for col in data.columnDicts -%}
    {{col.field_name}} = Column({{col.db_field_type}})
    {% endfor %}

    {% if (data.primary_key_fields is not none and data.primary_key_fields is iterable)%}
    __table_args__ = (
        PrimaryKeyConstraint(
        {%- for field in data.primary_key_fields -%}
            '{{field}}' {%- if not loop.last %},{%endif -%}
        {% endfor %}),
        {},
    )
    {% endif %}
