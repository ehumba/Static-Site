class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props == None:
            return ''
        attributes_string = ""
        for key, value in self.props.items():
            attributes_string += f' {key}="{value}"'
        return attributes_string
    def __repr__(self) -> str:
        return f"HTMLNode {self.tag, self.value, self.children, self.props}"
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, props)
        self.props = props
    
    def __repr__(self):
        return f"LeafNode({self.tag!r}, {self.value!r}, {self.props!r})"
    
    def to_html(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return f'{self.value}'
        props_html = self.props_to_html()
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'
