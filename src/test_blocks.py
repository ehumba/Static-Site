import unittest
from blocks import (markdown_to_blocks, block_to_block_type)


markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

print(markdown_to_blocks(markdown))

class TestMarkdownToHTML(unittest.TestCase):

    def test_block_to_block_types(self):
        block1 = "# Big Title"
        self.assertEqual(block_to_block_type(block1), "heading")
        block2 = "```\na_lot_of_code\nand_even_more_code\n```"
        self.assertEqual(block_to_block_type(block2), "code")
        block3 = ">veni\n>vidi\n>vici"
        self.assertEqual(block_to_block_type(block3), "quote")
        block4 = ">veni\nvidi\n>vici"
        self.assertEqual(block_to_block_type(block4), "paragraph")
        block5 = "* first\n* second\n* third"
        self.assertEqual(block_to_block_type(block5), "unordered_list")
        block6 = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block6), "ordered_list")

if __name__ == "__main__":
    unittest.main()