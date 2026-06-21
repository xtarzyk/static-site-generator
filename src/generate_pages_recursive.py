from os import listdir
from os.path import isfile, join
from pathlib import Path

from generate_content import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in listdir(dir_path_content):
        from_path = join(dir_path_content, filename)
        dest_path = join(dest_dir_path, filename)
        if isfile(from_path):
            generate_page(from_path, template_path, Path(dest_path).with_suffix(".html"))
        else:
            generate_pages_recursive(from_path, template_path, dest_path)