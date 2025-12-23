# Static Site Generator 

This is a static site generator built with Python, created as part of the [Boot.dev](https://www.boot.dev) curriculum. It converts a directory of Markdown files into a fully functional static website using a customizable HTML template.

## 🚀 About The Project

This project was built following the ["Build a Static Site Generator"](https://www.boot.dev/courses/build-static-site-generator-python) course on Boot.dev. The goal of the project is to understand the fundamentals of:
- Parsing text and Markdown syntax
- Recursive file processing
- Object-Oriented Programming in Python
- HTML generation and templating

## ✨ Features

- **Markdown to HTML Conversion**: Supports headings, bold/italic text, links, images, lists, blockquotes, and code blocks.
- **Recursive Page Generation**: Automatically mirrors the directory structure of your `content/` folder in the output.
- **Templating**: Wraps generated content in a `template.html` for consistent layout.
- **Static Asset Management**: Copies CSS and images from `static/` to the public directory.

## 📂 Project Structure

```
.
├── content/           # Your Markdown content lives here
├── static/            # Static assets (CSS, images)
├── docs/              # Generated site (output folder)
├── src/               # Source code
│   ├── main.py        # Entry point
│   ├── htmlnode.py    # HTML generation logic
│   ├── textnode.py    # Intermediate text representation
│   └── ...
├── template.html      # Base HTML template
├── main.sh            # Script for local development
└── build.sh           # Script for GitHub Pages deployment
```

## 🛠️ Usage

### Prerequisites

- Python 3.x

### Running Locally

To generate the site and serve it locally:

```bash
./main.sh
```

This will build the site into the `docs/` directory and start a local server at `http://localhost:8888`.

### Deploying to GitHub Pages

To build the site with the correct base path for GitHub Pages:

```bash
./build.sh
```

This script runs the generator with the `/static-site-generator/` base path configuration.

## 🧪 Running Tests

To run the unit tests:

```bash
./test.sh
```
