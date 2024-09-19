import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_2(self):
        node = ("Node1", "italics")
        node2 = ("Node2", "italics")
        self.assertNotEqual(node, node2)
    def test_3(self):
        node = ("some_node", "bold")
        node2 = ("some_node", "bold", "https://de.wikipedia.org/")
        self.assertNotEqual(node, node2)
    def test_4(self):
        node = ("eine_node", "normal", "https://de.wikipedia.org/")
        node2 = ("eine_node", "bold", "https://de.wikipedia.org/")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
