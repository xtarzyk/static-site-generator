import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Matching closing delimiter is not found")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        img_tuples = extract_markdown_images(node.text)
        
        if len(img_tuples) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for tuple in img_tuples:
            sections = original_text.split(f"![{tuple[0]}]({tuple[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(tuple[0], TextType.IMAGE, tuple[1]))
            original_text = sections[1]

        if original_text == "":
            continue
        new_nodes.append(TextNode(original_text, TextType.TEXT))  

    return new_nodes

    
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        link_tuples = extract_markdown_links(node.text)
        
        if len(link_tuples) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for tuple in link_tuples:
            sections = original_text.split(f"[{tuple[0]}]({tuple[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(tuple[0], TextType.LINK, tuple[1]))
            original_text = sections[1]

        if original_text == "":
            continue
        new_nodes.append(TextNode(original_text, TextType.TEXT))  

    return new_nodes