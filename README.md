# CodeMind AI — Coding Assistant

An AI-powered coding assistant built with Flask and the Gemini API. Supports real-time streaming responses, multiple AI personas, live HTML preview, and persistent chat history.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square)
![Gemini](https://img.shields.io/badge/Gemini-2.5--flash-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## Features

- **Streaming responses** — answers generate word by word in real time, just like ChatGPT
- **Three AI personas** — switch between Assistant, Code Reviewer, and Debugger modes, each with a different system prompt
- **Live HTML preview** — code blocks with HTML automatically show a "Preview" button that renders the output in a side panel
- **Persistent chat history** — conversations are saved locally and can be resumed anytime
- **Web search** — powered by Gemini's built-in Google Search tool for up-to-date answers
- **Collapsible sidebar** — clean minimal UI inspired by ChatGPT and Claude
- **Copy buttons** — every code block and response has a one-click copy button

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI | Google Gemini 2.5 Flash API |
| Frontend | Vanilla JS, HTML, CSS |
| Markdown | Marked.js |
| Syntax highlighting | Highlight.js |
| Deployment | Render |

---

## Getting Started

### Prerequisites

- Python 3.10+
- A [Gemini API key](https://aistudio.google.com/apikey) (free)

### Installation

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/codemind-ai.git
cd codemind-ai

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

### Run locally

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000`

---

## AI Personas

| Persona | Behavior |
|---|---|
| **Assistant** | General coding help, explanations, and code generation |
| **Code Reviewer** | Reviews code like a senior engineer — flags bugs, security issues, and bad practices with severity levels |
| **Debugger** | Identifies root cause of errors and returns a ready-to-paste fix |

---

## Project Structure

```
codemind-ai/
├── app.py              # Flask backend, streaming API route, persona prompts
├── requirements.txt    # Dependencies
├── .env                # API key (not committed)
├── .gitignore
└── templates/
    └── index.html      # Full frontend — UI, streaming, chat history
```

---

## Deployment

This project is configured for deployment on [Render]([https://render.com](https://codemind-ai-2pl9.onrender.com/)) (free tier).

1. Fork this repo
2. Create a new Web Service on Render and connect the repo
3. Add `GEMINI_API_KEY` as an environment variable
4. Deploy — Render auto-detects the configuration

---

## What I Learned

- Implementing **Server-Sent Events (SSE)** for real-time streaming in Flask
- **Prompt engineering** with different system prompts to control AI behavior
- Using the **Gemini `google-genai` SDK** for chat sessions with history
- Building a clean chat UI with **localStorage** for persistence without a database
- Deploying a Python web app to production with **Render**

---

## Author

Built by **Dinesh** as part of a portfolio project while applying to AI engineering roles.

- GitHub: [@Dineshv0311](https://github.com/Dineshv0311)

---

## License

MIT
