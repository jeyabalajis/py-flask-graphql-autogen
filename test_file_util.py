from utils import file_util
from os import path


class TestFileUtil:
    def test_copy_file(self):
        file_util.copy_file("template/database", "__init__.py", "out/database")
        assert path.exists("out/database" + "/" + "models.py")

    def test_copy_dir_tree(self):
        file_util.copy_tree("template/db_utils", "out/db_utils")
        assert path.exists("out/db_utils/db_session_maker.py")

    def test_create_dir(self):
        base_path = "E:/GraphQLPOC"
        root_folder_name = "schema-demo"
        file_util.create_dir(base_path, root_folder_name)
        assert path.exists(base_path + "/" + root_folder_name)

    def test_create_archive(self):
        source = "E:/GraphQLPOC"
        destination = "E:/GraphQLPOC/auto-graphql-demo.zip"
        file_util.make_archive(source, destination)
        assert path.exists(destination)
