import unittest

from htmlnode import *

parent = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
print(parent.__repr__())
print(parent.to_html())

parent3 = ParentNode("p", [ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)], {"href": "https://www.google.com", "target": "_blank"})

print(parent3.__repr__())
print(parent3.to_html())

class TestParentNode(unittest.TestCase):
    def test1(self):
        node1 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        node2 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node1, node2)
    def test2(self): 
        node1 = ParentNode("p", [ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)], {"href": "https://www.google.com", "target": "_blank"})
        node2 = ParentNode("p", [ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)
