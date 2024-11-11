from extract_markdown import *
from split_nodes import *

def text_to_textnodes(text):
    node_list = [TextNode(text, "text")]
    node_list = split_nodes_delimiter(node_list, "**", "bold")
    node_list = split_nodes_delimiter(node_list, "*", "italics")
    node_list = split_nodes_delimiter(node_list, "`", "code")
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)
    return node_list
