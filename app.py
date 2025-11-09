import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history = []
MAX_HISTORY = 5

def generate_response(prompt):
    history.append(prompt)
    recent_history = history[-MAX_HISTORY:]
    final_prompt = "\n".join(recent_history)

    data = {
        "model": "iris",
        "prompt": final_prompt,
        "stream": False  # no streaming needed for button click
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        data = response.json()
        return data["response"]
    else:
        return f"Error: {response.text}"

# Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt..."),
    outputs=gr.Textbox(lines=20, placeholder="Model response will appear here...")  # bigger output box
)

interface.launch()
