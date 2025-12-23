# Static Site Generator

A Python-based static site generator that converts Markdown files into HTML pages.

## Features

- Convert Markdown to HTML
- Recursive page generation
- Template-based HTML output
- Support for common Markdown syntax:
  - Headings
  - Bold and italic text
  - Links and images
  - Code blocks
  - Ordered and unordered lists
  - Blockquotes

## Project Structure

```
static-site-generator/
├── content/           # Markdown source files
├── static/            # Static assets (CSS, images)
├── public/            # Generated HTML output
├── template.html      # HTML template
└── src/
    ├── main.py        # Entry point
    ├── htmlnode.py    # HTML node classes
    ├── textnode.py    # Text node handling
    └── markdown_to_html.py  # Markdown conversion
```

## Usage

### Basic Usage

```bash
./main.sh
```

### With Custom Base Path

```bash
python src/main.py /custom-path/
```

## How It Works

1. Copies static files from `static/` to `public/`
2. Recursively converts all `.md` files in `content/` to `.html`
3. Applies `template.html` to each generated page
4. Serves the site on `http://localhost:8888`

## Requirements

- Python 3.x

## Running Tests

```bash
python -m unittest discover -s src
```