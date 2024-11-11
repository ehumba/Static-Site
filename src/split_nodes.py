from textnode import *
import re
from extract_markdown import *

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        satz = node.text
        teile = extract_markdown_images(satz)
        if len(teile) == 0:
            new_nodes.append(node)
        for bild in teile:
            sections = satz.split(f"[{bild[0]}]({bild[1]})", 1)
            #Schau an was das macht
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], 'text'))
            new_nodes.append(TextNode(bild[0], "image", bild[1],))
            satz = sections[1]
        if satz != "":
            new_nodes.append(TextNode(satz, "text"))
    return new_nodes
   
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        satz = node.text
        teile = extract_markdown_links(satz)
        if len(teile) == 0:
            new_nodes.append(node)
        for link in teile:
            sections = satz.split(f"[{link[0]}]({link[1]})", 1)
            
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], 'text'))
            new_nodes.append(TextNode(link[0], "link", link[1],))
            satz = sections[1]
        if satz != "":
            new_nodes.append(TextNode(satz, "text"))
    return new_nodes