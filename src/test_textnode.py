import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "None")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_again(self):
        node = TextNode("This is a text node", "bold", "https://www.bootdev.dev")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_again(self):
        node = TextNode("This is a text node", "bold", "https://www.bootdev.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.bootdev.dev")
        self.assertEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", "image", "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_link(self):
        node = TextNode("This is a link", "link", "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.__repr__(), f"LeafNode(a, This is a link, {html_node.props})")

if __name__ == "__main__":
    unittest.main()
