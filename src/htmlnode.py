class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        if len(self.props) <= 0:
            return ""
        res = ""
        for key in self.props.keys():
            res += f" {key}=\"{self.props[key]}\""
        return res
    
    def __repr__(self):
        return f"""HTML Node: 
        • Tag: {self.tag}
        • Value: {self.value}
        • Children: {self.children}
        • Properties: {self.props}
        """