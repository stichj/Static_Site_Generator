import re
from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if (
            self.text == other.text 
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            new_nodes.extend(split_single_node(node, delimiter, text_type))
    return new_nodes

def split_single_node(node, delimiter, text_type):
    text = node.text.split(delimiter)
    if len(text) % 2 != 1:
        raise Exception(f"Illegal Markdown syntax: Missing closing / opening '{delimiter}'")
    
    split_nodes = []
    for i in range(len(text)):
        if text[i] == "":
            continue
        if i % 2 == 0:
            split_nodes.append(TextNode(text[i], TextType.TEXT))
        else:
            split_nodes.append(TextNode(text[i], text_type))
    return split_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        
        if node.text is None or node.text == "":
            continue
        matches = extract_markdown_images(node.text)
        
        if not matches:
            new_nodes.append(TextNode(node.text, node.text_type, node.url))
            continue
        
        curr_string = node.text

        for alt_text, url in matches:
            nodes, rest = compose_text_node_list(alt_text, url, curr_string, node.text_type, TextType.IMAGE)
            new_nodes.extend(nodes)
            curr_string = rest
            
        if curr_string:
            new_nodes.append(TextNode(curr_string, node.text_type, node.url))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        
        if not node.text:
            continue
        matches = extract_markdown_links(node.text)
        
        if not matches:
            new_nodes.append(TextNode(node.text, node.text_type, node.url))
            continue
        
        curr_string = node.text
        for alt_text, url in matches:
            nodes, rest = compose_text_node_list(alt_text, url, curr_string, node.text_type, TextType.LINK)
            new_nodes.extend(nodes)
            curr_string = rest
            
        if curr_string:
            new_nodes.append(TextNode(curr_string, node.text_type, node.url))
    return new_nodes

def compose_text_node_list(alt_text, url, text, regular_text_type, link_type):
    new_nodes = []
    if link_type is TextType.LINK:
        split = text.split(f'[{alt_text}]({url})', maxsplit=1)
    elif link_type is TextType.IMAGE:
        split = text.split(f'![{alt_text}]({url})', maxsplit=1)
    else:
        raise TypeError("Illegal TextType provided")
    
    if not split:
        new_nodes.append(TextNode(alt_text, link_type, url))
        return new_nodes

    if split[0]:
        new_nodes.append(TextNode(split[0], regular_text_type))
    
    new_nodes.append(TextNode(alt_text, link_type, url))
    
    return new_nodes, split[1]

def text_to_text_nodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    delimiters = [('**', TextType.BOLD), ('_', TextType.ITALIC), ('`', TextType.CODE)]
    
    for delimiter, text_type in delimiters:
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes