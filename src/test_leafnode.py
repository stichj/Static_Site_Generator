import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    def test_leaf_to_html_empty_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()
    def test_leaf_to_html_none_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")
    def test_leaf_to_html_empty_tag(self):
        node = LeafNode("", "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")
    def test_leaf_to_html_properties(self):
        props={
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode("a", "Hello World!", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Hello World!</a>')