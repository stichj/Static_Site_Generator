from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("Tag missing")
        if self.children is None or not self.children:
            raise ValueError("Missing children")
        
        html_text = f"<{self.tag}>"
        if not self.props is None or self.props:
            html_text = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html_text += child.to_html()
            
        html_text += f"</{self.tag}>"
        
        return html_text