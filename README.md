# 📊 InsightGen – AI-Powered Data Analysis Assistant (Runs 100% Locally)

InsightGen is your personal data analyst – built with Gradio and powered by local LLMs using Ollama (like Mistral or LLaMA 2). It allows you to upload a CSV file and ask natural language questions about your data. The app returns Python code, plain-English explanations, and even chart instructions — all **without any internet or API keys**.

---

## 🚀 Features

✅ Upload your own CSV file  
✅ Ask questions in plain English like:  
&nbsp;&nbsp;&nbsp;&nbsp;• *"What is the average age of patients?"*  
&nbsp;&nbsp;&nbsp;&nbsp;• *"Show a bar chart of patients by Site_ID"*  
✅ Get back:
- Python code using pandas
- Step-by-step explanation
- Expected output description

✅ Powered by open-source LLMs (e.g. Mistral via Ollama)  
✅ Built with Python + Gradio  
✅ 100% runs locally (no OpenAI key required)

---

## 🧠 How It Works

1. **Upload CSV**: Load a dataset like `Patient.csv`.
2. **Gradio UI**: Shows a preview and suggests smart questions.
3. **Ask a Question**: Enter a natural language prompt.
4. **Ollama Response**: A local LLM converts your question into pandas code and explanations.
5. **Insight Display**: You get the generated code and insight in the UI.

---

## 💻 Local Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/InsightGen.git
cd InsightGen
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```
Make sure ollama is installed: https://ollama.com

3. Start Ollama
```bash
ollama run mistral
```

4. Run the App
```bash
python app.py
```

Visit: http://localhost:7860

🛠️ Tech Stack
🧠 Ollama – Local LLM runtime
🤖 Mistral / LLaMA 2 – LLM models
🐼 Pandas – Data analysis
🖼️ Gradio – User interface
📊 Matplotlib / Seaborn (future: for chart rendering)

📌 Roadmap
 Add support for plotting charts
 Enable voice-to-question (Whisper)
 Add RAG support for multi-file analysis
 Export insights to PDF
 Session memory (chat history)
