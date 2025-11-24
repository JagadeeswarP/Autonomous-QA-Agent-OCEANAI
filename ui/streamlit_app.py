import streamlit as st
import requests
import json

API_URL = "http://localhost:8000"

st.title("Autonomous QA Agent")

# -----------------------------------------
# File Upload
# -----------------------------------------
st.header("📤 Upload Documents")
uploaded = st.file_uploader("Upload Support Docs + checkout.html", accept_multiple_files=True)

if uploaded:
    for f in uploaded:
        files = {"file": (f.name, f.read())}
        try:
            r = requests.post(f"{API_URL}/upload", files=files)
            resp = r.json()
            st.success(resp.get("message", "Uploaded"))
        except Exception as e:
            st.error("❌ Backend returned invalid JSON during upload")
            st.write(r.text)


# -----------------------------------------
# Generate Test Cases
# -----------------------------------------
st.header("🧠 Generate Test Cases")
query = st.text_input("Enter Feature or Scenario:")

if st.button("Generate Test Cases"):
    try:
        r = requests.post(f"{API_URL}/generate_test_cases", data={"query": query})
        resp = r.json()

        if "result" in resp:
            st.code(json.dumps(resp["result"], indent=2), language="json")
        else:
            st.error("❌ Backend did not return 'result'")
            st.write(resp)

    except Exception as e:
        st.error("❌ Backend returned invalid JSON")
        st.write("Raw response:")
        try:
            st.code(r.text)
        except:
            st.write("No response received")


# -----------------------------------------
# Generate Selenium Script
# -----------------------------------------
st.header("🧪 Generate Selenium Script")
test_case_input = st.text_area("Paste Selected Test Case JSON")

if st.button("Generate Script"):
    try:
        r = requests.post(f"{API_URL}/generate_script", data={"test_case": test_case_input})
        resp = r.json()

        if "result" in resp:
            st.code(resp["result"], language="python")
        else:
            st.error("❌ Backend did not return 'result'")
            st.write(resp)

    except Exception:
        st.error("❌ Backend returned invalid JSON")
        st.write("Raw response:")
        try:
            st.code(r.text)
        except:
            st.write("No response received")
