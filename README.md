# 🌌 Galaxy Project

This repository contains the seed codebase for the **Galaxy** project built with **Python**, **Flask**, **SQLAlchemy**, and **Pytest**. It includes features like workout planning, real-time chat, Google Maps integration, and an AI chatbot.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aysinakpinar/Galaxy_gym_python_flask.git
```

### 2. Set Up Virtual Environment

```bash
python -m venv galaxy_venv
source galaxy_venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
pip install playwright
```

> **Note**: If you encounter a `ModuleNotFoundError`, deactivate and reactivate your virtual environment. If issues persist, contact your coach.

---

## 🔐 Environment Variables

This project uses a `.env` file to store sensitive environment variables like the **Google Maps API key**.

### 1. Create a `.env` File in the Project Root

```bash
touch .env
```

### 2. Add Your Google Maps API Key

Inside the `.env` file, add:

```env
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
```

### 3. Load Environment Variables

Ensure you’re using a library like `python-dotenv` (included in `requirements.txt`) and have this in your config or app setup:

```python
from dotenv import load_dotenv
load_dotenv()
```

Then, access the key like:

```python
import os
api_key = os.getenv("GOOGLE_MAPS_API_KEY")
```

> Never commit your `.env` file to version control. Add it to `.gitignore`.

---

## ⚙️ Database Setup

### 1. Create Databases

```bash
createdb galaxy_db
createdb galaxy_db_test
```

### 2. Run Migrations

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. Seed the Databases

```bash
python seeds/0_user_seed.py
python seeds/1_friendship_seed.py
python seeds/2_user_point_seed.py
python seeds/3_exercise_seed.py
python seeds/4_quote_seed.py
python seeds/5_gym_seed.py
python seeds/6_workout_seed.py
python seeds/7_workout_exercise_seed.py
```

---

## 🧠 AI Chatbot Setup (Mistral 7B)

Uses [Mistral 7B](https://ollama.com/library/mistral) via [Ollama](https://ollama.com/).

### Instructions

1. **Install Ollama**:
   ```bash
   brew install ollama
   ```

2. **Start Ollama**:
   ```bash
   ollama start
   ```

3. **Download the Mistral Model**:
   ```bash
   ollama pull mistral:7b-instruct-q4_K_M
   ```

4. **Serve the Model**:
   ```bash
   ollama serve
   ```

5. **Run the Flask App in a Separate Terminal**:
   ```bash
   flask run
   ```

> Keep `ollama serve` running. The chatbot may respond with some delay (~9s).

---

## 💬 Real-Time Chat (Socket.IO)

### Install Required Packages

```bash
pip install flask-socketio python-socketio eventlet
```

These are already included in `requirements.txt`.

### Features

- Real-time private messaging
- Active user tracking
- Automatic room joining/switching
- SocketIO server integration (`app.py`)
- Interface handled by `messages.html` and `chat.py`

Use this to start your app:

```python
socketio.run(app, debug=True)
```

---

## 📁 Project Structure

```text
.
├── README.md
├── .env                    # Environment variables (not committed)
├── app.py                  # Entry point
├── blueprints/             # Business logic
├── config.py               # Environment config
├── extension.py
├── forms/                  # User input forms
├── models/                 # Database tables
├── requirement.txt
├── static/                 # Static assets (CSS/JS)
├── templates/              # HTML templates
├── tests/                  # Test suite
└── venv/                   # Virtual environment
```

---

## 🧪 Run Tests

```bash
pytest -sv
```

---

## 🖥️ Run the App

```bash
python app.py
```

Then open: [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home)

---

