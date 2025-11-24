import os
from dotenv import load_dotenv

load_dotenv()

LLM_URL = os.getenv("LLM_URL", "http://localhost:1234/v1/chat/completions")
MODEL_NAME = os.getenv("MODEL_NAME", "qwen3-1.7b")
