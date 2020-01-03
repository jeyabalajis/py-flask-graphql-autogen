from flask import Flask, request
from services.graphql_service import generate_server_service

app = Flask(__name__)
app.debug = True


@app.route("/generate_server/<app_name>", methods=['POST'])
def generate_server(app_name):
    body = request.get_json()
    return generate_server_service(app_name=app_name, tables_metadata=body)


if __name__ == '__main__':
    app.run()
