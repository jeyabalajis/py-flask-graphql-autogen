from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader("template")
env = Environment(loader=file_loader)


def render_template(path: str, file_name: str, data: dict) -> str:
    template = env.get_template(path + "/" + file_name)
    output = template.render(data=data)
    return output
