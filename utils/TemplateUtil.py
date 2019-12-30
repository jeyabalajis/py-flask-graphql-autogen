from jinja2 import Environment, FileSystemLoader
from setup.config import TEMPLATE_FOLDER
from utils.file_util import write_to_file
import black
import os


class TemplateUtil:
    file_loader = FileSystemLoader(TEMPLATE_FOLDER)
    env = Environment(loader=file_loader)

    def __init__(self, template_path: str, template_file_name: str, data: dict):
        self.template_path = template_path
        self.template_file_name = template_file_name
        self.data = data

    def render_template(self) -> str:
        template = self.env.get_template(self.template_path + "/" + self.template_file_name)
        output = template.render(data=self.data)
        return output

    def render_template_to_file(self, out_file_path: str, out_file_name: str):
        output = self.render_template()
        write_to_file(out_file_path, out_file_name, output)
        try:
            os.system('black ' + './' + out_file_path + "/" + out_file_name)
        except OSError as e:
            print("Install black for auto formatting" + e.strerror)
        finally:
            pass
