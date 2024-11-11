import unittest

from textnode import TextNode
from htmlnode import *
from main import text_node_to_html_node
from split_nodes import *
from extract_markdown import *
from text_to_textnodes import text_to_textnodes

anode = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text",)
print(split_nodes_link([anode]))
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
bnode = TextNode(
    "This is text with a link [to a newspaper](https://www.derstandard.at/)",
    "text",)
print(split_nodes_link([bnode]))

cnode = TextNode(
    "This is text with a link to a newspaper https://www.derstandard.at/",
    "text",)
print(split_nodes_link([cnode]))

dnode = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "link",)
print(split_nodes_link([dnode]))

enode = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
print(split_nodes_image([enode]))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]



node = TextNode("This is text with a `code block` word", "text")
print(split_nodes_delimiter([node], "`", "code"))

node3 = TextNode("This is text with a **bold** word", "text")
print(split_nodes_delimiter([node3], "**", "bold"))

node5 = TextNode("This is text with an *italic* word", "text")
print(split_nodes_delimiter([node5], "*", "italic"))

tested_node1 = TextNode("This is a text node", "bold")
tested_node2 = TextNode("Node1", "italics")
tested_node3 = TextNode("It is working", "text", None)
tested_node4 = TextNode("This is code", "code", None)
tested_node5 = TextNode("some_node", "link", "https://de.wikipedia.org/")
tested_node6 = TextNode("some_node", "image", "https://de.wikipedia.org/")

print(text_node_to_html_node(tested_node1))
print(text_node_to_html_node(tested_node2))
print(text_node_to_html_node(tested_node3))
print(text_node_to_html_node(tested_node4))
print(text_node_to_html_node(tested_node5))
print(text_node_to_html_node(tested_node6))

def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", "Text"),
                TextNode("text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "italic"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
            ],
            nodes,
        )