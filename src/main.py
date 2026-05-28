from htmlnode import HTMLNode
from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    htmlnode = HTMLNode("p", "Some text")
    print(node)
    print(htmlnode)

if __name__ == "__main__":
    main()
