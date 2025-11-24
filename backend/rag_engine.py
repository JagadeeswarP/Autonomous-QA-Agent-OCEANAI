import requests
import re
import json

LLM_URL = "use your local LLM endpoint here"
MODEL_NAME = "use any model name here"

SYSTEM_PROMPT = """
You are a strict agent.
Never output <think> or chain-of-thought.
Only output the final answer exactly in JSON or code format.
"""


# Below remove_think is used for small models that may output <think>...<think> , because I have noticed
# that some smaller models tend to add chain-of-thought even when instructed not to. For larger models,
# this function can be commented out.
# def remove_think(text):
#     # Remove <think>...</think>
#     cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

#     # Remove garbage before '[' or '{'
#     cleaned = re.sub(r"^[\s\S]*?([\[\{])", r"\1", cleaned, flags=re.DOTALL)

#     # Remove trailing garbage after last ']' or '}'
#     last_json_end = max(cleaned.rfind("]"), cleaned.rfind("}"))
#     if last_json_end != -1:
#         cleaned = cleaned[: last_json_end + 1]

#     return cleaned.strip()


def ask_llm(prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 1500
    }

    response = requests.post(LLM_URL, json=payload)

    print("\n\n🔵 RAW LLM OUTPUT:\n", response.text)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "LLM returned invalid response:\n" + response.text


def generate_test_cases(feature_text, html_text):

    prompt = f"""
Generate detailed test cases in JSON format ONLY.

Feature/Scenario: {feature_text}

HTML of the page:
{html_text}

Output JSON array only. No explanations.
"""

    output = ask_llm(prompt)

   # cleaned = remove_think(output)

    try:
        # return json.loads(cleaned) for small models
        return json.loads(output)
    except:
        # return {"error": "Model returned invalid JSON", "raw_output": cleaned} for small models
        return {"error": "Model returned invalid JSON", "raw_output": output}

def generate_selenium_script(test_case_json, html_text):

    prompt = f"""
Create a Selenium Python script for this test case.

Test Case JSON:
{json.dumps(test_case_json, indent=2)}

HTML:
{html_text}

Rules:
- Output ONLY Python code. No explanations.
"""

    script = ask_llm(prompt)
    # script = remove_think(script)


    return script
