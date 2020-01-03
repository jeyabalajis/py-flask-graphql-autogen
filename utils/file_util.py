import os
import shutil
from distutils.dir_util import copy_tree


def get_fq_path(file_path: str, file_name: str = None) -> str:
    """
    join path with a file name
    """
    return file_path + "/" + file_name if file_name else file_path


def write_to_file(file_path: str, file_name: str, file_content: str):
    """
    write string contents into a file
    """
    os.makedirs(os.path.dirname(get_fq_path(file_path, file_name)), exist_ok=True)
    try:
        with open(get_fq_path(file_path, file_name), 'w') as f:
            f.write(file_content)
    except Exception as e:
        print("Error! {}".format(str(e)))
    finally:
        f.close()


def copy_file(file_path: str, file_name: str, out_path: str, out_file_name: str = None):
    """
    copy file from one folder to another
    """
    os.makedirs(os.path.dirname(get_fq_path(out_path, out_file_name)), exist_ok=True)
    source = get_fq_path(file_path, file_name)
    destination = get_fq_path(out_path, out_file_name)
    shutil.copy(source, destination)


def copy_dir_tree(from_dir: str, to_dir: str):
    """
    copy contents from one directory to another
    """
    copy_tree(from_dir, to_dir)


def create_dir(base_path: str, root_folder_name: str):
    """
    create a directory if it does not exist
    """
    dir_name = get_fq_path(base_path, root_folder_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print("Directory ", dir_name, " Created ")
    else:
        print("Directory ", dir_name, " already exists")


def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    archive_format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    print(source, destination, archive_from, archive_to)
    shutil.make_archive(name, archive_format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, archive_format), destination)
