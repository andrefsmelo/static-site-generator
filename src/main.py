import os
import shutil
import sys
from markdown_to_html import markdown_to_html_node, extract_title


def copy_files(source, destination):
    if os.path.exists(destination):
        print(f"Cleaning {destination} directory.")
        shutil.rmtree(destination)
    os.mkdir(destination)

    for file in os.listdir(source):
        source_path = os.path.join(source, file)
        dest_path = os.path.join(destination, file)

        print(f"Copying file: {source_path} -> {dest_path}")

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_files(source_path, dest_path)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    html = html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
            f.write(html)


def generates_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, file)
        if os.path.isfile(source_path) and file.endswith(".md"):
            html_filename = file.replace(".md", ".html")
            dest_path = os.path.join(dest_dir_path, html_filename)
            print(f"Markdown found: {source_path}")
            generate_page(source_path, template_path, dest_path, basepath)
        if not os.path.isfile(source_path):
            new_dest = os.path.join(dest_dir_path, file)
            generates_pages_recursive(source_path, template_path, new_dest, basepath)


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_files("static", "docs")
    generates_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
