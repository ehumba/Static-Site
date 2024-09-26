import unittest

from htmlnode import HTMLNode


tested_node = HTMLNode('<a>', 'some text', None, {"href": "https://www.google.com", "target": "_blank"})
print(tested_node.__repr__())
print(tested_node.props_to_html())

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node1 = HTMLNode('<a>', 'some text', ["Kind1", "Kind2"], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode('<a>', 'some text', ["Kind1", "Kind2"], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)
    def test2(self): 
        node1 = HTMLNode('<a>', 'some text', ["Kind1", "Kind2"], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode('<a>', 'some text', None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node1, node2)
    def test3(self):
        node1 = HTMLNode('<a>', 'some text', ["Kind1", "Kind2"], {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode('<a>', 'some text', ["Kind1", "Kind2"], None)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()