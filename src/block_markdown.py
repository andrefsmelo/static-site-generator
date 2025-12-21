from enum import Enum
import re

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block.strip() != ""]

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.heading
    if re.match(r"^```[\s\S]*```$", block):
        return BlockType.code
    if re.match(r"^(>.*\n?)+$", block):
        return BlockType.quote
    if re.match(r"^([*-] .*\n?)+$", block):
        return BlockType.unordered_list
    if block.startswith("1. "):
        i = 1
        for line in block.split("\n"):
            if not line.startswith(f"{i}. "):
                return BlockType.paragraph
            i += 1
        return BlockType.ordered_list
    return BlockType.paragraph