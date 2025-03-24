import os

from markdownblock import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    if not os.path.exists(from_path) or not os.path.isfile(from_path):
        raise FileNotFoundError(from_path, "not found or is not a file.")
    if not os.path.exists(template_path) or not os.path.isfile(template_path):
        raise FileNotFoundError(template_path, "not found or is not a file.")
    
    with open(from_path) as file:
        md_contents = file.read()
    with open(template_path) as file:
        html_template = file.read()
        
    html_code = markdown_to_html_node(md_contents).to_html()
    title = extract_title(md_contents)
    
    html_template = html_template.replace("{{ Title }}", title)
    html_template = html_template.replace("{{ Content }}", html_code)
    
    if not os.path.exists(os.path.dirname(dest_path)) or not os.path.isdir(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
        
    
    with open(dest_path, "w") as f:
        f.write(html_template)