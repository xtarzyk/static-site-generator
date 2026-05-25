import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type(self):
        node = TextNode("AAAAAAAAAAAAAAAA", TextType.BOLD)
        node2 = TextNode("bbbbbbbbbbb", TextType.BOLD)
        self.assertEqual(node.text_type, node2.text_type)

    def test_wrong_text_type(self):
        node = TextNode("AAAAAAAAAAAAAAAA", TextType.BOLD)
        node2 = TextNode("bbbbbbbbbbb", TextType.ITALIC)
        self.assertNotEqual(node.text_type, node2.text_type)

    

if __name__ == "__main__":
    unittest.main()