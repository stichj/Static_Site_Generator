from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(markdown):
    if markdown[0] == "#":
        i = 0
        char = markdown[i]
        while char == "#":
            i += 1
            char = markdown[i]
        
        if 1 <= i and 6 >= i and markdown[i] == " ":
            return BlockType.HEADING
    if (
        markdown[0] == "`"
        and markdown[1] == "`"
        and markdown[2] == "`"
        and markdown[-1] == "`"
        and markdown[-2] == "`"
        and markdown[-3] == "`"
    ):
        return BlockType.CODE
    
    if markdown[0] == ">":
        lines = markdown.split("\n")
        
        for line in lines:
            if line[0] != ">" and line[1] != " ":
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if markdown[0] == "-":
        lines = markdown.split("\n")
        
        for line in lines:
            if line[:2] != "- ":
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if markdown[0] == "1":
        lines = markdown.split("\n")
        
        for i, line in enumerate(lines):
            if line[:3] != f"{i+1}. ":
                return BlockType.PARAGRAPH
            
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
        
    