import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        node3 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node3)
        
        node.url = "https://www.boot.dev"
        node2.url = "https://www.boot.dev"
        self.assertEqual(node, node2)
        
        node4 = TextNode("This is a text node ", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node4)
        
        node.url = None
        node5 = TextNode("This is a text node", TextType("bold"))
        self.assertEqual(node, node5)
        
        node5.text_type = TextType.ITALIC
        self.assertNotEqual(node, node5)


if __name__ == "__main__":
    unittest.main()