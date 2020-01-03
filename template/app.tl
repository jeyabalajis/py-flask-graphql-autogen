from flask import Flask
from flask_graphql import GraphQLView

from database.models import db_session
from schema.schema import schema

app = Flask(__name__)
app.debug = True

{# Inject application name as part of path #}
app.add_url_rule(
    '/{{data.app_name}}/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
