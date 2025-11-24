import fitz
import markdown
import json
from bs4 import BeautifulSoup

def parse_pdf(file_bytes):
    doc = fitz.open("pdf", file_bytes)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_md(md_text):
    return md_text

def parse_txt(text):
    return text

def parse_json(json_text):
    data = json.loads(json_text)
    return json.dumps(data, indent=2)

def parse_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    clean_text = soup.get_text(separator="\n")
    return clean_text
