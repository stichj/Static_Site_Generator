import unittest

from htmlnode import * 

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")
        
    def test_props_to_html_neq(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertNotEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
    def test_props_to_html(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")