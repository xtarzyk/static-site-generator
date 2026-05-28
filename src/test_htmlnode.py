import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", None, None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_props(self):
        node = HTMLNode("a", None, None, {"href": "https://www.google.com"})
        node2 = HTMLNode("a", None, None, {"href": "https://www.google.com"})
        self.assertEqual(node.props, node2.props)

    def test_diff_tags(self):
        node = HTMLNode("body")
        node2 = HTMLNode("ul", None, HTMLNode("li"), None)
        self.assertNotEqual(node, node2)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_html_label(self):
        node = LeafNode("label", "Label text", {"for": "inputName"})
        self.assertEqual(node.to_html(), '<label for="inputName">Label text</label>')
    

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    

if __name__ == "__main__":
    unittest.main()