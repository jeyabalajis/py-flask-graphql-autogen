from core.GraphQLTable import GraphQLTable
from utils.TemplateUtil import TemplateUtil
from utils.file_util import create_dir, copy_file, copy_dir_tree, get_fq_path
from static.config import (
    DB_MODELS_FOLDER,
    GRAPHQL_SCHEMA_FOLDER,
    GRAPHQL_SERVER_FOLDER,
    BLIND_COPY_FILES,
    BLIND_COPY_FOLDERS
)


class GraphQLServer:
    def __init__(self, app_name: str, base_path: str, root_folder_name: str, table_meta_data: [dict]):
        self.app_name = app_name
        self.base_path = base_path
        self.root_folder_name = root_folder_name
        assert isinstance(table_meta_data, list) and len(table_meta_data) > 0
        self.table_meta_data = table_meta_data

    def generate_graphql_server(self):
        """
        1. Generate database models
        2. Generate GraphQL schema
        3. Generate app.py
        4. Copy other files
        """
        # use each table json to create a GraphQLTable instance and store its members as a JSON through __dict__
        tables = [GraphQLTable.from_json(_table_json).__dict__ for _table_json in self.table_meta_data]

        data = {
            "db_models_folder": DB_MODELS_FOLDER,  # required to handle the imports in other files
            "tables": tables,
            "app_name": self.app_name,
        }

        # Create the project folder if it does not exist
        create_dir(self.base_path, self.root_folder_name)

        _project_root = get_fq_path(self.base_path + "/" + self.root_folder_name)
        _db_folder = get_fq_path(_project_root, DB_MODELS_FOLDER)
        _schema_folder = get_fq_path(_project_root, GRAPHQL_SCHEMA_FOLDER)

        # Generate database models
        template_util = TemplateUtil(DB_MODELS_FOLDER, "models.tl", data)
        template_util.render_template_to_file(
            _db_folder,
            "models.tl".replace(".tl", ".py")
        )

        # Generate schema schema
        template_util = TemplateUtil(GRAPHQL_SCHEMA_FOLDER, "schema.tl", data)
        template_util.render_template_to_file(
            _schema_folder,
            "schema.tl".replace(".tl", ".py")
        )

        # Generate GraphQL Server file
        template_util = TemplateUtil(".", "app.tl", data)
        template_util.render_template_to_file(
            _project_root,
            "app.tl".replace(".tl", ".py")
        )

        # Blind copy files
        for _copy_unit in BLIND_COPY_FILES:
            copy_file(_copy_unit["source_path"], _copy_unit["source_file"], _copy_unit["target"].format(_project_root))

        # Blind copy folders
        for _folder in BLIND_COPY_FOLDERS:
            copy_dir_tree(_folder["source"], _folder["target"].format(_project_root))
