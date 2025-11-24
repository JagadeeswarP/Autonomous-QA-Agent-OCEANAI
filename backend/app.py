from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from parser_utils import *
from vector_store import add_to_vector_db
from rag_engine import generate_test_cases, generate_selenium_script
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

html_cache = ""  

@app.post("/upload")
async def upload(file: UploadFile):
    global html_cache

    content = await file.read()

    if file.filename.endswith(".pdf"):
        text = parse_pdf(content)

    elif file.filename.endswith(".md"):
        text = parse_md(content.decode())

    elif file.filename.endswith(".txt"):
        text = parse_txt(content.decode())

    elif file.filename.endswith(".json"):
        text = parse_json(content.decode())

    elif file.filename.endswith(".html"):
        text = parse_html(content.decode())
        html_cache = content.decode()   

    else:
        return {"error": "Unsupported format"}

    add_to_vector_db(text, {"id": file.filename, "source": file.filename})

    return {"message": f"{file.filename} uploaded & indexed."}


@app.post("/generate_test_cases")
async def tc(query: str = Form(...)):
    global html_cache

    response = generate_test_cases(query, html_cache)

    return {"result": response}


@app.post("/generate_script")
async def script(test_case: str = Form(...)):
    global html_cache

    try:
        tc_json = json.loads(test_case)
    except:
        return {"error": "Invalid test case JSON"}

    response = generate_selenium_script(tc_json, html_cache)

    return {"result": response}
