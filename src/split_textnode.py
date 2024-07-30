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