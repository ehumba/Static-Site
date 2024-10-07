import unittest

from htmlnode import *


tested_node = LeafNode("a", "tested text", {"href": "https://www.google.com", "target": "_blank"})
tested_node2 = LeafNode("p", "another test", None)
print(tested_node.__repr__())
print(tested_node.to_html())
print(tested_node2.to_html())


class TestLeafNode(unittest.TestCase):
    def test1(self):
        node1 = LeafNode('a', 'some text', {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode('a', 'some text', {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)
    def test2(self): 
        node1 = LeafNode('a', 'some text', None)
        node2 = LeafNode('a', 'some text', None)
        self.assertEqual(node1, node2)
    def test3(self):
        node1 = LeafNode('a', 'some text', {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode('a', 'some text', None)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()