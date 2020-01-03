import tempfile
from core.GraphQLServer import GraphQLServer
from utils import file_util, response_util
import base64


def generate_server_service(*, app_name, tables_metadata: dict):
    base_path = tempfile.mkdtemp()
    root_folder_name = app_name

    try:
        graph_ql_server = GraphQLServer(
            app_name=app_name,
            base_path=base_path,
            root_folder_name=root_folder_name,
            table_meta_data=tables_metadata
        )
    except AssertionError:
        return response_util.get_response(status=400, title="Error", detail="Invalid Metadata Input")

    graph_ql_server.generate_graphql_server()

    destination = base_path + "/" + app_name + ".zip"
    file_util.make_archive(base_path, destination)

    with open(destination, "rb") as file_in:
        zip_read = file_in.read()
        encoded = base64.b64encode(zip_read)

    return response_util.get_response(status=200, title="Success", detail=encoded.decode("utf-8"))

