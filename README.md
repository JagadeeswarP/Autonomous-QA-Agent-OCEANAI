<!DOCTYPE html>
<html lang="en">

<body>
<div class="container">

<h1 align="center">✨ Autonomous QA Agent</h1>
<h3 align="center">AI-Powered Test Case Generator & Selenium Script Automation</h3>

<p class="badge-row" align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/LLM-AI%20Driven-FFB000?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

<hr>

<h2>🚀 Overview</h2>
<p>
This project is an <strong>Autonomous QA Agent</strong> that automatically reads documentation,
interprets UI screens, generates <strong>test cases</strong>, produces <strong>Selenium scripts</strong>,
and lets you run them in a browser to validate PASS/FAIL results.
</p>

<p>All outputs are fully grounded in this uploaded project files — no hallucinations.</p>

<hr>

<h2>🧠 How It Works</h2>

<pre>
Docs + HTML → LLM → JSON Test Cases
Test Case → LLM → Selenium Script
Script → Browser → PASS / FAIL
</pre>

<p>The agent behaves like a real QA engineer — understanding requirements and designing automation tests.</p>

<hr>

<h2>📁 Project Structure</h2>

<pre>
autonomous-qa-agent/
│
├── backend/
│   ├── app.py
│   ├── rag_engine.py
│   ├── parser_utils.py
│   ├── vector_store.py
│   ├── requirements.txt
│   └── chroma_db/
│
├── ui/
│   ├── streamlit_app.py
│
├── checkout.html
├── product_specs.md
├── api_endpoints.json
├── ui_ux_guide.txt
│
├── generated_scripts/
└── README.md
</pre>

<hr>

<h2>⚙️ Installation</h2>

<h3>1️⃣ Clone the repository</h3>
<pre><code>git clone https://github.com/your-username/autonomous-qa-agent.git
cd autonomous-qa-agent</code></pre>

<h3>2️⃣ Install dependencies</h3>
<pre><code>pip install -r backend/requirements.txt</code></pre>

<h3>3️⃣ Configure environment</h3>
<p>Create a <code>.env</code> file:</p>

<pre><code>
LLM_URL=http://127.0.0.1:1234/v1/chat/completions
MODEL_NAME=qwen3-1.7b:2
</code></pre>

<hr>

<h2>▶️ Running the Project</h2>

<h3>🔥 Start FastAPI backend</h3>
<pre><code>cd backend
uvicorn app:app --reload</code></pre>

<p>Backend runs at:</p>
<pre><code>http://127.0.0.1:8000</code></pre>

<h3>🎨 Start Streamlit frontend</h3>
<pre><code>cd ui
streamlit run streamlit_app.py</code></pre>

<p>UI runs at:</p>
<pre><code>http://localhost:8501</code></pre>

<hr>

<h2>🧪 Generate Test Cases</h2>

<p>Example prompt:</p>

<pre><code>Generate positive and negative test cases for the discount code feature.</code></pre>

<p>Example output:</p>

<pre><code>{
  "Test_ID": "TC-001",
  "Scenario": "Valid discount code",
  "Input": { "discount-code": "SAVE10" },
  "Expected": { "discount-error": "" }
}</code></pre>

<hr>

<h2>🤖 Generate Selenium Scripts</h2>

<p>Paste test case JSON → Receive fully runnable Selenium code:</p>

<pre><code>
driver.find_element(By.ID, "discount-code").send_keys("SAVE10")
assert driver.find_element(By.ID, "discount-error").text == ""
</code></pre>

<p>Selenium scripts auto-save into:</p>

<pre><code>generated_scripts/</code></pre>

<hr>

<h2>🛠 Running a Selenium Test</h2>

<pre><code>python generated_scripts/TC-001.py</code></pre>

<ul>
  <li>Opens Chrome</li>
  <li>Loads your HTML</li>
  <li>Runs automation</li>
  <li>Validates assertions</li>
  <li>Prints <strong>PASS / FAIL</strong></li>
</ul>

<hr>

<h2>📦 Dependencies</h2>

<ul>
  <li>Python 3.10+</li>
  <li>FastAPI</li>
  <li>Streamlit</li>
  <li>Selenium</li>
  <li>ChromaDB</li>
  <li>SentenceTransformers</li>
  <li>BeautifulSoup4</li>
</ul>

<hr>

<h2>📝 Support Documents Explanation</h2>

<table border="1" cellspacing="0" cellpadding="8">
<tr><th>File</th><th>Purpose</th></tr>
<tr><td>checkout.html</td><td>UI for Selenium automation</td></tr>
<tr><td>product_specs.md</td><td>Functional requirements</td></tr>
<tr><td>api_endpoints.json</td><td>API specs</td></tr>
<tr><td>ui_ux_guide.txt</td><td>UX rules & guidelines</td></tr>
<tr><td>PDF files</td><td>High-level documentation</td></tr>
</table>

<hr>

<h2>👨‍💻 Author</h2>

<p><strong>Jagadeeswar Pattupogula</strong><br>
B.Tech CSE • AI & Automation Enthusiast</p>

</div>
</body>
</html>
