from htmlnode import HTMLNode, LeafNode

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, target):
		if (self.text == target.text and
		self.text_type == target.text_type and
		self.url == target.url):
			return True
		else:
			return False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text, None)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception(f"Not a matching text type: {text_node.text_type}")

def main():
	test = TextNode("This is a test", "bold", "https://www.boot.dev")
	print(test.__repr__())

main()
