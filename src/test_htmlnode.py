import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_true1(self):
        node1 = HTMLNode("hi", 21, None, {"href": "https://www.bootdev.dev", "target": "_blank",})
        testing_string = node1.props_to_html()
        print(testing_string)
        self.assertTrue(isinstance(testing_string, str))
    def test_true2(self):
        node2 = HTMLNode("hi", 21, None, {"href": "https://www.bootdev.dev", "target": "_blank",})
        testing_string2 = node2.__repr__()
        print(testing_string2)
        self.assertTrue(isinstance(testing_string2, str))
    def test_true3(self):
        node3 = HTMLNode("hi")
        testing_string = node3.props_to_html()
        self.assertEqual(testing_string, "")
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    def test_to_html_with_many_grandchildren(self):
        child_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>",
        )
    def test_headings(self):
        node = ParentNode(
            "hello",
            [
                LeafNode("Goodbye", "Farewells"),
                LeafNode(None, "Small talk"),
                LeafNode(None, "Small talk"),
                LeafNode("Goodbye", "Farewells"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<hello><Goodbye>Farewells</Goodbye>Small talkSmall talk<Goodbye>Farewells</Goodbye></hello>",
        )


if __name__ == "__main__":
    unittest.main()