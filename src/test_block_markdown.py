import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_whitespace(self):
        md = "   \n\nBlock 1\n\n   \n\nBlock 2"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Block 1",
                "Block 2",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)
        block = "###### heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)
        block = "####### paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_block_to_block_type_code(self):
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)
        block = "```python\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)

    def test_block_to_block_type_quote(self):
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.quote)
        block = "> quote"
        self.assertEqual(block_to_block_type(block), BlockType.quote)

    def test_block_to_block_type_unordered_list(self):
        block = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)
        block = "* item 1\n* item 2"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)
        
    def test_block_to_block_type_ordered_list(self):
        block = "1. item 1\n2. item 2"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)
        block = "1. item 1\n3. item 3" # Incorrect numbering
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_block_to_block_type_paragraph(self):
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)
        block = "-not a list"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

if __name__ == "__main__":
    unittest.main()
