from textnode import *


def main():
    text_node = TextNode("This is some anchor text", TextType("link"), "https:boot.dev")
    
    print(text_node)
    
    
    
if __name__ == "__main__":
    main()