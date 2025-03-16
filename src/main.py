from textnode import *
from htmlnode import *


def main():
    text_node = TextNode("This is some anchor text", TextType("link"), "https:boot.dev")
    
    print(text_node)
    
    html_node = HTMLNode("Tag", "Value", props={
    "href": "https://www.google.com",
    "target": "_blank",
    })
    
    print(html_node)
    print(html_node.props_to_html())
    
if __name__ == "__main__":
    main()