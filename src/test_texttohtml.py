import unittest

from textnode import TextNode
from htmlnode import *
from main import text_node_to_html_node
from split_nodes import *

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