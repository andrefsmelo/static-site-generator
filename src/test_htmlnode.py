import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a", 
            "Link", 
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_values(self):
        node = HTMLNode("p", "Olá mundo")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Olá mundo")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("h1", "Título", None, {"id": "main"})
        expected = "HTMLNode(h1, Título, None, {'id': 'main'})"
        self.assertEqual(repr(node), expected)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just raw text here")
        self.assertEqual(node.to_html(), "Just raw text here")

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_to_html_void_element(self):
        node = LeafNode("img", None, {"src": "image.png", "alt": "test"})
        self.assertEqual(node.to_html(), '<img src="image.png" alt="test">')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                ParentNode("span", [LeafNode(None, "Nested text")]),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i><span>Nested text</span></p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_parent_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("span", "content")],
            {"class": "container", "id": "main-div"}
        )
        expected = '<div class="container" id="main-div"><span>content</span></div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_errors(self):
        node_no_tag = ParentNode(None, [LeafNode("b", "test")])
        with self.assertRaises(ValueError) as cm:
            node_no_tag.to_html()
        self.assertEqual(str(cm.exception), "Invalid HTML: ParentNode must have a tag")

        node_no_children = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            node_no_children.to_html()
        self.assertEqual(str(cm.exception), "Invalid HTML: ParentNode must have children")

if __name__ == "__main__":
    unittest.main()