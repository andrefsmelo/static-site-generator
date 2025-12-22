import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading with **bold**

## Heading with _italic_ and `code`

###### Small heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading with <b>bold</b></h1><h2>Heading with <i>italic</i> and <code>code</code></h2><h6>Small heading</h6></div>",
        )

    def test_blockquote(self):
        md = """
> This is a **bold** quote
> with _italic_ text
> and `code` too
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><p>This is a <b>bold</b> quote with <i>italic</i> text and <code>code</code> too</p></blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- item with **bold**
- item with _italic_
- item with `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item with <b>bold</b></li><li>item with <i>italic</i></li><li>item with <code>code</code></li></ul></div>",
        )

    def test_unordered_list_asterisk(self):
        md = """
* first with [link](https://example.com)
* second with ![image](img.png)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>first with <a href=\"https://example.com\">link</a></li><li>second with <img src=\"img.png\" alt=\"image\"></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. first with **bold**
2. second with _italic_
3. third with `code`
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first with <b>bold</b></li><li>second with <i>italic</i></li><li>third with <code>code</code></li></ol></div>",
        )

    def test_codeblock_with_language(self):
        md = "```python\ndef foo():\n    pass\n```"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>def foo():\n    pass\n</code></pre></div>",
        )

    def test_mixed_content(self):
        md = "# Title\n\nSome **bold** text\n\n- list item"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Title</h1><p>Some <b>bold</b> text</p><ul><li>list item</li></ul></div>",
        )


if __name__ == "__main__":
    unittest.main()