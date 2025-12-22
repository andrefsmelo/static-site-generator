from block_markdown import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import ParentNode
from inline_markdown import text_to_text_nodes
from textnode import text_node_to_html_node, TextNode, TextType
import re

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.paragraph:
            return ParentNode(tag="p", children=text_to_children(block.replace("\n", " ")))
        case BlockType.heading:
            match = re.match(r"#+", block)
            n = len(match[0]) if match else 1
            return ParentNode(tag=f"h{n}", children=text_to_children(block.lstrip("#").strip()))
        case BlockType.code:
            lines = block.split("\n")
            content = "\n".join(lines[1:-1]) + "\n"
            node = text_node_to_html_node(TextNode(content, TextType.TEXT))
            return ParentNode(tag="pre", children=[ParentNode(tag="code", children=[node])])
        case BlockType.quote:
            content = " ".join(line.lstrip(">").strip() for line in block.split("\n"))
            return ParentNode(tag="blockquote", children=text_to_children(content))
        case BlockType.unordered_list:
            items = [ParentNode(tag="li", children=text_to_children(line[2:])) for line in block.split("\n")]
            return ParentNode(tag="ul", children=items)
        case BlockType.ordered_list:
            lines = [ParentNode(tag="li", children=text_to_children(re.sub(r"^\d+\.\s+", "", line))) for line in block.split("\n")]
            return ParentNode(tag="ol", children=lines)
        
        case _:
            return ParentNode(tag="p", children=text_to_children(block))


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = [block_to_html_node(block, block_to_block_type(block)) for block in blocks]
    return ParentNode(tag="div", children=html_nodes)


def extract_title(markdown):
    first_line = markdown.split("\n")[0]
    if first_line.startswith("#"):
        return first_line.lstrip("#").strip()
    raise Exception("Markdown Title not found.")