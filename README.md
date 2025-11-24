✨ Autonomous QA Agent
<h3 align="center">AI-Powered Test Case Generator & Selenium Script Automation</h3> <p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white" /> <img src="https://img.shields.io/badge/LLM-AI%20Driven-FFB000?style=for-the-badge" /> <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" /> </p>
<section> <h2>🚀 <strong>Overview</strong></h2> <p> This project is an <strong>Autonomous QA Agent</strong> that automatically reads documentation, interprets the UI, generates <strong>test cases</strong>, produces <strong>Selenium scripts</strong>, and allows you to run them in a real browser to validate PASS/FAIL results. </p> <p> All outputs are fully <strong>grounded</strong> in actual project files — HTML, product specs, UX guidelines, and API details. No hallucinations. No assumptions. Only real, actionable automation. </p> </section>
<section> <h2>🧠 <strong>How It Works</strong></h2> <pre> Docs + HTML → LLM → JSON Test Cases Test Case → LLM → Selenium Script Script → Browser → PASS / FAIL </pre> <p> The agent behaves like a real QA engineer — reading documents, designing tests, and writing automation scripts. </p> </section>
<section> <h2>📁 <strong>Project Structure</strong></h2> <pre> autonomous-qa-agent/ │ ├── backend/ │ ├── app.py │ ├── config.py │ ├── parser_utils.py │ ├── rag_engine.py │ ├── vector_store.py │ ├── requirements.txt │ └── chroma_db/ │ ├── ui/ │ ├── streamlit_app.py │ ├── checkout.html │ ├── product_specs.md │ ├── api_endpoints.json │ └── ui_ux_guide.txt │ ├── generated_scripts/ ├── .env.example ├── .gitignore └── README.md </pre> </section>
<section> <h2>⚙️ <strong>Installation</strong></h2> <h3>1️⃣ Clone the repository</h3> <pre><code>git clone https://github.com/&lt;your-username&gt;/autonomous-qa-agent.git cd autonomous-qa-agent </code></pre> <h3>2️⃣ Install dependencies</h3> <pre><code>pip install -r backend/requirements.txt </code></pre> <h3>3️⃣ Configure environment variables</h3> <pre><code>cp .env.example .env </code></pre>

Fill in:

<pre><code>LLM_URL=http://localhost:1234/v1/chat/completions MODEL_NAME=qwen3-1.7b </code></pre> <h3>4️⃣ Start backend</h3> <pre><code>python backend/app.py </code></pre> <h3>5️⃣ Launch UI</h3> <pre><code>streamlit run ui/streamlit_app.py </code></pre> </section>
<section> <h2>🧪 <strong>Generating Test Cases</strong></h2>

Type in:

<pre><code>Generate positive and negative test cases for the discount feature.</code></pre>

Example output:

<pre><code>[ { "scenario": "Valid discount code applied", "input": { "discount-code": "SAVE15" }, "expected_output": { "discount-applied": 15, "final-total": 85.00 } } ]</code></pre> </section>
<section> <h2>🤖 <strong>Generating Selenium Scripts</strong></h2> <p>Choose a test case — the agent generates a fully runnable Selenium test:</p> <pre><code>driver.find_element(By.ID, "discount-code").send_keys("SAVE15") driver.find_element(By.ID, "apply-discount").click() assert float(driver.find_element(By.ID, "total-price").text) == 85.00 </code></pre>

Scripts are stored in:

generated_scripts/

</section>
<section> <h2>🛠 <strong>Run the Selenium Test</strong></h2>

Just execute:

<pre><code>python generated_scripts/TC-001.py </code></pre>

The script:

<ul> <li>Opens your browser</li> <li>Loads checkout.html</li> <li>Inputs values</li> <li>Clicks buttons</li> <li>Reads totals</li> <li>Validates assertions</li> <li>Prints PASS / FAIL</li> </ul> </section>
<section> <h2>📦 <strong>Dependencies</strong></h2> <ul> <li>Python 3.10+</li> <li>Selenium WebDriver</li> <li>Streamlit</li> <li>Requests</li> <li>BeautifulSoup4</li> <li>ChromaDB</li> </ul> </section>
<section> <h2>🔐 <strong>.gitignore</strong></h2> <pre><code> .venv/ __pycache__/ .env backend/chroma_db/ generated_scripts/ test_results/ .vscode/ .DS_Store </code></pre> </section>
<section> <h2>👨‍💻 <strong>Author</strong></h2> <p> <strong>Jagadeeswar Pattupogula</strong><br> B.Tech CSE Student • AI & Automation Enthusiast<br> Focused on building intelligent QA tools and automation systems. </p> </section>
<section> <h2>📄 <strong>License</strong></h2> <p>MIT License</p> </section>
