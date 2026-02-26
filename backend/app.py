from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import sqlite3

app = Flask(__name__)
CORS(app)

# ---- DATABASE FOR CACHE ----
def init_db():
    conn = sqlite3.connect("chat_cache.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---- CHAT ROUTE ----
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    

    # Check cache first
    conn = sqlite3.connect("chat_cache.db")
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM chat_cache WHERE question=?", (user_message,))
    result = cursor.fetchone()

    if result:
        conn.close()
        return jsonify({"reply": result[0], "cached": True})

    # If not cached → Ask Ollama
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "qwen2.5-coder:3b",
                "messages": [
                    {"role": "user", "content": user_message}
                ],
                "stream": False
            }
        )

        ai_reply = response.json()["message"]["content"].strip()

        # Save to cache
        cursor.execute(
            "INSERT INTO chat_cache (question, answer) VALUES (?, ?)", 
            (user_message, ai_reply)
        )
        conn.commit()
        conn.close()

        return jsonify({"reply": ai_reply, "cached": False})

    except Exception:
        conn.close()
        return jsonify({
            "reply": "AI service temporarily unavailable.",
            "cached": False
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)