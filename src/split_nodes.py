from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_type_text = "text"
    text_type_code = "code"
    text_type_bold = "bold"
    text_type_italics = "italics"
    text_type_link = "link"
    text_type_image = "image"
    new_nodes = []
    for nodes in old_nodes:
        if nodes.text_type != "text":
            new_nodes.append(nodes)
        split_text = nodes.text.split(delimiter)
        no_delimiter = split_text[0::2]
        in_delimiter = split_text[1::2]
        if len(split_text) % 2 == 0:
            raise Exception("No closing delimiter found")

        for stueck in split_text:
            if stueck in no_delimiter:
                new_nodes.append(TextNode(f'{stueck}', "text_type.text"))
            if stueck in in_delimiter:
                new_nodes.append(TextNode(f'{stueck}', f'text_type.{text_type}'))
        
    return new_nodes