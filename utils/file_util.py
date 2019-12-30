import os
import shutil
from distutils.dir_util import copy_tree


def __get_fq_path(file_path: str, file_name: str = None) -> str:
    """
    join path with a file name
    """
    return file_path + "/" + file_name if file_name else file_path


def write_to_file(file_path: str, file_name: str, file_content: str):
    """
    write string contents into a file
    """
    os.makedirs(os.path.dirname(__get_fq_path(file_path, file_name)), exist_ok=True)
    try:
        with open(__get_fq_path(file_path, file_name), 'w') as f:
            f.write(file_content)
    except Exception as e:
        print("Error! {}".format(str(e)))
    finally:
        f.close()


def copy_file(file_path: str, file_name: str, out_path: str, out_file_name: str = None):
    """
    copy file from one folder to another
    """
    os.makedirs(os.path.dirname(__get_fq_path(out_path, out_file_name)), exist_ok=True)
    destination = out_path + "/" + out_file_name if out_file_name else out_path
    shutil.copy(__get_fq_path(file_path, file_name), out_path)


def copy_dir_tree(from_dir: str, to_dir: str):
    """
    copy contents from one directory to another
    """
    copy_tree(from_dir, to_dir)
