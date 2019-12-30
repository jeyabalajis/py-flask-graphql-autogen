from utils import file_util
from os import path


class TestFileUtil:
    def test_copy_file(self):
        file_util.copy_file("template/database", "__init__.py", "out/database")
        assert path.exists("out/database" + "/" + "models.py")

    def test_copy_dir_tree(self):
        file_util.copy_tree("template/db_utils", "out/db_utils")
        assert path.exists("out/db_utils/db_session_maker.py")
