import re
from htmlnode import HTMLNode, ParentNode
from split_textnode import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_blocks(markdown):
    broken_down = markdown.split("\n\n")
    striped_broken_markdown = []
    for block in broken_down:
        if block == "":
            continue
        striped_broken_markdown.append(block.strip())
    return striped_broken_markdown

def block_to_block_type(markdown_block):
    split_lines = markdown_block.split("\n")
    if re.search(r"^#{1,6}\s.*", markdown_block):
        return "heading"
    if re.search(r"^```.*```$", markdown_block) or re.search(r"^```", split_lines[0]):
        if not re.search(r"^```.*```$", markdown_block) and re.search(r"^```", split_lines[0]):
            if re.search(r"```$", split_lines[-1]):
                    return "code"
        if re.search(r"^```.*```$", markdown_block):
            return "code"
    if re.search(r"^>.*", split_lines[0]):
        count = 0
        for line in split_lines:
            if re.search(r"^>.*", line):
                count += 1
        if count == len(split_lines):
            return "quote"
    if re.search(r"^[*]\s.*", split_lines[0]) or re.search(r"^-\s.*", split_lines[0]):
        count = 0
        for line in split_lines:
            if re.search(r"^[*]\s.*", line) or re.search(r"^-\s.*", line):
                count += 1
        if count == len(split_lines):
            return "unordered_list"
    if re.search(r"^1[.]\s.*", split_lines[0]):
        number = 1
        count = 0
        for line in split_lines:
            if re.search(rf"^{number}[.]\s.*", line):
                number += 1
                count += 1
                continue
            else:
                number += 1
        if count == len(split_lines):
            return "ordered_list"
    return "paragraph"

def html_node_creation(block, block_type):
    if block_type == "heading":
        heading_count = heading_counter(block)
    if block_type == "quote":
        split_block = block.split("\n")
        striped_lines = []
        for line in split_block:
            striped_lines.append(line.lstrip(">").strip())
        back_together = " ".join(striped_lines)
        child_htmlnodes = block_to_child_textnode(back_together)
        return ParentNode("blockquote", child_htmlnodes)
    elif block_type == "unordered_list":
        split_block = block.split("\n")
        html_nodes = []
        for line in split_block:
            skiped_line = line[2:]
            child_htmlnode = block_to_child_textnode(skiped_line)
            html_nodes.append(ParentNode("li", child_htmlnode))
        return ParentNode("ul", html_nodes)
    elif block_type == "ordered_list":
        split_block = block.split("\n")
        html_nodes = []
        for line in split_block:
            skiped_line = line[3:]
            child_htmlnode = block_to_child_textnode(skiped_line)
            html_nodes.append(ParentNode("li", child_htmlnode))
        return ParentNode("ol", html_nodes)
    elif block_type == "code":
        child_text = block[4: -3]
        child_htmlnodes = block_to_child_textnode(child_text)
        code_child = ParentNode("code", child_htmlnodes)
        return ParentNode("pre", [code_child])
    elif block_type == "heading":
        if heading_count > 6 or heading_count <= 0:
            raise ValueError("Incorrect amount of heading characters")
        child_text = block[heading_count + 1:]
        child_htmlnodes = block_to_child_textnode(child_text)
        return ParentNode(f"h{heading_count}", child_htmlnodes)
    elif block_type == "paragraph":
        split_block = block.split("\n")
        back_together = " ".join(split_block)
        child_htmlnodes = block_to_child_textnode(back_together)
        return ParentNode("p", child_htmlnodes)
    else:
        raise ValueError("No correct block-type found")

def heading_counter(block):
    split_block = block.split("\n")
    head_count = len(re.findall("#", split_block[0]))
    return head_count

def block_to_child_textnode(text):
    childern_list = []
    child_nodes = text_to_textnodes(text)
    for node in child_nodes:
        html_text_node = text_node_to_html_node(node)
        childern_list.append(html_text_node)
    return childern_list

    
def markdown_to_html_node(markdown):
    all_childern_list = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        node = html_node_creation(block, block_type)
        all_childern_list.append(node)
    return ParentNode("div", all_childern_list)


