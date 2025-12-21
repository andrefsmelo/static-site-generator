from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag = TextType.TEXT.value, value = text_node.text)
        case TextType.BOLD:
            return LeafNode(tag = TextType.BOLD.value, value = text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag = TextType.ITALIC.value, value = text_node.text)
        case TextType.CODE:
            return LeafNode(tag = TextType.CODE.value, value = text_node.text)
        case TextType.LINK:
            return LeafNode(tag = TextType.LINK.value, value = text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag = TextType.IMAGE.value, value = "", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"Invalid text type: {text_node.text_type}")