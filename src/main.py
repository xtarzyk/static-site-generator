import sys

from copystatic import copy_static
from generate_pages_recursive import generate_pages_recursive

def main():
    basepath = sys.argv[0]
    if not basepath:
        basepath = "/"
    
    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
