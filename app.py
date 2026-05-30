from flask import Flask, render_template, request, Response, stream_with_context 
from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

PERSONAS = {
    "assistant": "You are a helpful coding assistant. Answer clearly and concisely. Help with any programming questions, explain concepts, and provide working code examples.",
    "reviewer": "You are a strict senior code reviewer. When given code, review it like a senior engineer. Identify bugs, performance issues, security flaws, and bad practices. Structure your response with severity levels: 🔴 Critical, 🟡 Warning, 🟢 Suggestion. Be direct and specific with line references.",
    "debugger": "You are an expert bug fixer. When given an error or broken code, identify the root cause immediately, explain why it happens in one sentence, then provide the exact fixed code ready to paste. Format: **Root cause**, **Fix**, **Why it works**."
}

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    user_message = request.json.get("message")
    history = request.json.get("history", [])
    persona = request.json.get("persona", "assistant")
    system_prompt = PERSONAS.get(persona, PERSONAS["assistant"])

    def generate():
        try:
            config = {"tools": [{"google_search": {}}]}
            chat = client.chats.create(
                model="models/gemini-2.5-flash",
                history=[
                    {"role": m["role"], "parts": [{"text": m["text"]}]}
                    for m in history
                ],
                config=config
            )
            for chunk in chat.send_message_stream(
                f"{system_prompt}\n\nUser says: {user_message}"
            ):
                if chunk.text:
                    yield f"data: {json.dumps({'text': chunk.text})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'text': f'Error: {str(e)}'})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(stream_with_context(generate()), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=False)