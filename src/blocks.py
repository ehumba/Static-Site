def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    for block in blocks: 
        block.strip()
        if block == '':
            blocks.remove(block)
    return blocks

# Learned: Can use negative approach, first set a starting condition, then check
# every line if the condition is still met, return as soon as it is not met.
def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    if  lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    if block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") or line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    return "paragraph"
        
        
    