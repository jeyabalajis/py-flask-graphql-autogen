from flask import Flask, request, jsonify
from services.graphql_service import generate_server_service
from flask_cors import CORS

app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET'])
def say_hello():
    return jsonify(status=200, detail="Hello!")


@app.route("/generate_server/<app_name>", methods=['POST'])
def generate_server(app_name):
    body = request.get_json()
    return generate_server_service(app_name=app_name, tables_metadata=body)


CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
