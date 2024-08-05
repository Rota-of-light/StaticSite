import os
from static_to_public import Static_to_Public
from generator import generate_page, generate_page_recursive

def main():
    Static_to_Public()
    generate_page_recursive("content", "template.html", "public")

main()
