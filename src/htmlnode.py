class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        attributes_string = ""
        for key, value in self.props.items():
            attributes_string += f' {key}="{value}"'
        return attributes_string
    def __repr__(self) -> str:
        return f"HTMLNode {self.tag, self.value, self.children, self.props}"
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        
