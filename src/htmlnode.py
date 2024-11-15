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


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if children is None:
            raise ValueError('ParentNode must have children')
        super().__init__(tag, children, props)
        self.children = children

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('No tag found')
        if self.children is None:
            raise ValueError('ParentNode must have children')
        html = ''
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}>{html}</{self.tag}>"

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == "italics":
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == "code":
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Unsupported type")