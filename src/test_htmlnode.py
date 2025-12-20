import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a", 
            "Link", 
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected = ' href=https://www.google.com target=_blank'
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
    
if __name__ == "__main__":
    unittest.main()