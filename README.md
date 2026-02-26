# TeamTrinity_AI-Data-Smart-Systems

## 👥 Team Name
**Team Trinity**

## 🚀 Project Name
**Trinity AI – Low Bandwidth Chatbot**

## 🧠 Track
AI, Data & Smart Systems

---

## 📌 Problem Statement

### Low-Bandwidth AI Assistant for Rural Areas

Many rural areas face poor internet connectivity and limited access to advanced AI platforms. Modern AI systems require high-speed internet and powerful infrastructure, making them inaccessible for students and teachers in low-resource regions.

This creates a digital divide where rural learners cannot benefit from AI-powered education tools.

Trinity AI solves this by providing a lightweight AI assistant that runs locally using a small language model, requiring minimal internet bandwidth.

---

## 💡 Solution Overview

Trinity AI is an offline-capable AI assistant designed for rural environments.

Instead of relying on cloud APIs, it uses a locally hosted language model via Ollama, reducing bandwidth usage and enabling deployment in low-connectivity areas.

It also includes:
- SQLite-based local caching
- Greeting detection for fast responses
- Optimized short-answer responses
- Low-resource backend architecture

---

## 🏗️ Architecture

User → Frontend (HTML/CSS/JS) → Flask Backend → Ollama Local LLM → SQLite Cache

The model runs locally to ensure minimal internet dependency.

---

## 🛠️ Tech Stack

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python (Flask)
- SQLite (Local Cache)

AI Model:
- Ollama
- qwen2.5-coder:3b (locally hosted)

---

## ⚙️ Setup Instructions

### 1️⃣ Install Ollama
Download from:
https://ollama.com

### 2️⃣ Pull the Model

ollama pull qwen2.5-coder:3b


### 3️⃣ Start Ollama

ollama run qwen2.5-coder:3b


(Then press Ctrl+C to stop after confirming it works.)


### 4️⃣ Run Backend

python app.py


### 5️⃣ Run Frontend
Open `index.html` using Live Server or your preferred method.

---

## 📶 Why Low Bandwidth?

- No cloud API calls required
- Model runs locally
- Responses are short and optimized
- Cache reduces repeated computation
- Designed for rural offline environments

---

## 👨‍💻 Team Members

Krishna Verma – Frontend & AI Integration  
Devansh Gupta – Frontend & UI/UX  
Divyanshu Sharma – Backend Developer  

---

## 📌 Note

This project requires Ollama and the qwen2.5-coder:3b model to be installed locally.

The AI engine runs fully offline to support rural low-bandwidth deployment scenarios.

---
