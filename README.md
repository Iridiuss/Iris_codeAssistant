🧠 Iris Code Assistant — Powered by CodeLlama

This project is a lightweight AI code assistant interface built with Python and Gradio.
It connects to a local model endpoint and generates context-aware code or text responses based on user prompts.

🚀 Overview

The app provides a simple web interface where users can:

Type any programming or text prompt

Send it to a locally running model API

Receive generated responses instantly in the UI

The assistant maintains a short conversation history to keep responses relevant to recent context.

⚙️ How It Works

The frontend is built using Gradio, providing an intuitive chat-style interface.

User prompts are sent to a local API endpoint (e.g., http://localhost:11434/api/generate).

The assistant aggregates the last few prompts to form context before sending requests.

The model returns a structured JSON response that is displayed in the interface.

<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/7516b3bc-4f6b-4207-a654-6404497b7466" />

