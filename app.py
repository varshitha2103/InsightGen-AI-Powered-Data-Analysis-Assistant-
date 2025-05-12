import gradio as gr
import pandas as pd
import requests

global_df = None

# Talk to Ollama locally
def call_ollama(prompt):
    import requests
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]

# Load CSV
def load_csv(file):
    global global_df
    global_df = pd.read_csv(file.name)
    preview = global_df.head().to_markdown()
    return preview, suggest_questions(global_df)

# Suggest questions based on columns
def suggest_questions(df):
    columns = df.columns.tolist()
    if not columns:
        return "No columns found."

    suggestions = [
        f"• What is the average age of patients?",
        f"• How many patients are in each site?",
        f"• What is the gender ratio in the dataset?"
    ]
    return "\n".join(suggestions)  # ✅ This fixes the Markdown error

# Ask a question
def ask_question(question):
    try:
        if global_df is None:
            return "⚠️ Please upload a dataset first."

        sample = global_df.head(10).to_string(index=False)
        prompt = f"""
You are a Python data analyst.
Here is a preview of the dataset:

{sample}

User question: "{question}"

Provide:
1. Python code using pandas
2. An explanation of what the code does
3. A short summary of expected results
"""
        result = call_ollama(prompt)
        return result

    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 📊 InsightGen – Your Local AI Data Analyst (No API Key Needed)")

    with gr.Row():
        file = gr.File(label="📂 Upload your CSV")
        preview = gr.Markdown()
        suggestions = gr.Markdown()

    file.change(fn=load_csv, inputs=file, outputs=[preview, suggestions])

    question = gr.Textbox(label="🧠 Ask a question about your data")
    response = gr.Markdown(label="🧾 Answer + Code")

    question.submit(fn=ask_question, inputs=question, outputs=response)

demo.launch()
