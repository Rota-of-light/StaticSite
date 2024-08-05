from markdown_breakdown import markdown_to_html_node, extract_title
from htmlnode import HTMLNode
import os
import re

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path)
    template = template_file.read()
    template_file.close()
    html_markdown = markdown_to_html_node(markdown)
    html_string = html_markdown.to_html()
    template_content = template.replace("{{ Content }}", html_string)
    title = extract_title(markdown)
    title_and_content = template_content.replace("{{ Title }}", title)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    html_page = open(dest_path, "w")
    html_page.write(title_and_content)
    html_page.close()

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    content_direct = os.listdir(dir_path_content)
    for item in content_direct:
        if item == "":
            continue
        new_item = os.path.join(dir_path_content, item)
        new_dest = os.path.join(dest_dir_path, item)
        if not os.path.isfile(new_item):
            generate_page_recursive(new_item, template_path, new_dest)
        else:
            file_type = re.findall(r"[.].*", item)
            file_dest = new_dest.replace(file_type[0], ".html")
            generate_page(new_item, template_path, file_dest)



