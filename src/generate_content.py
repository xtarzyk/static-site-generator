from os import makedirs
from os.path import dirname
from htmlnode import ParentNode
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith(("# ", "#")):
            return line[2:]
    raise Exception("No h1 header found!")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md:
        markdown = md.read()

    with open(template_path) as tmp:
        template = tmp.read()

    html = ParentNode.to_html(markdown_to_html_node(markdown))
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dir_path = dirname(dest_path)
    if dir_path != "":
        makedirs(dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(template)