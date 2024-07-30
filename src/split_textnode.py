import re
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    other_text_types = ["bold", "italic", "code", "link", "image"]
    new_nodes = []
    if not (text_type in other_text_types or text_type == "text"):
        raise Exception("Given text_type is not found")
    for node in old_nodes:
        if node.text_type in other_text_types:
            new_nodes.append(node)
            continue
        if node.text_type == "text" and delimiter not in node.text:
            new_nodes.append(node)
            continue
        if node.text_type == "text":
            broken_node_list = []
            broken_texts = node.text.split(delimiter)
            if len(broken_texts) % 2 == 0:
                raise Exception("Matching encapsulating delimiters not found")
            for i in range(len(broken_texts)):
                if broken_texts[i] == "":
                    continue
                if i % 2 == 0:
                    broken_node_list.append(TextNode(broken_texts[i], "text"))
                else:
                    broken_node_list.append(TextNode(broken_texts[i], text_type))
            new_nodes.extend(broken_node_list)
        else:
            raise Exception("Not matching any known text type")
    return new_nodes

def extract_markdown_images(text):
    extracted_list = []
    image_info = re.findall(r"!\[(.*?)\]", text)
    image_url = re.findall(r"\((.*?)\)", text)
    for i in range(len(image_info)):
        image_tuple = (image_info[i], image_url[i],)
        extracted_list.append(image_tuple)
    return extracted_list

def extract_markdown_links(text):
    extracted_list = []
    link_info = re.findall(r"\[(.*?)\]", text)
    link_url = re.findall(r"\((.*?)\)", text)
    for i in range(len(link_info)):
        link_tuple = (link_info[i], link_url[i],)
        extracted_list.append(link_tuple)
    return extracted_list