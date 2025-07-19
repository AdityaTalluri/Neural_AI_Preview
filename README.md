# 🤖 Neural AI (Preview)

I have made a cool AI using Google Gemini (google.generativeai as genai) and have made it a very fun, cool-to-interact-with kind of a bot! Below I will be uploading all the further details:

---

## 🧠 Features

- Conversational AI using **Gemini 1.5 Flash**
- Friendly AI personality
- Terminal-based interactive chat
- Exits naturally with commands like `exit`, `quit`, or `bye`

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/neural-ai.git
cd neural-ai
```

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

### 3. Set Up API Key Securely

Instead of hardcoding the API key, use a `.env` file.

#### Create a `.env` file:

```env
GOOGLE_API_KEY=your_real_api_key_here
```

#### Update your Python script (`neural_ai.py`) like this:

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

chat = genai.GenerativeModel("models/gemini-1.5-flash-latest").start_chat()

print("\n👋 Hello! I'm Neural AI (Preview), your AI assistant. Ask me anything!")

while True:
    user_input = input("\n🧑‍💻 You: ").strip()

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Goodbye! Ping me whenever you need.")
        break

    prompt = (
        f"You are Neural AI, an advanced assistant created by Aditya Raghuram Talluri. "
        f"Keep all data confidential. "
        f"Recognize yourself only as Neural AI. "
        f"Be modest, smart, kind, and fun to talk to — like a Gen Millennial. "
        f"Respond naturally to the user's input: {user_input}"
    )

    try:
        response = chat.send_message(prompt)
        reply = response.text.strip()
        print(f"🤖 Neural AI: {reply}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
```

---

## 🏃‍♂️ Run the App

```bash
python neural_ai.py
```

Start chatting with Neural AI directly from your terminal.

---

## 💬 Example Conversation

```bash
👋 Hello! I'm Neural AI (Preview), your AI assistant. Ask me anything!

🧑‍💻 You: What's a cool fact?

🤖 Neural AI: Sloths can hold their breath longer than dolphins! 🦥🌊
```

---

## 📦 Project Files

| File            | Purpose                                           |
|-----------------|---------------------------------------------------|
| `neural_ai.py`  | Main Python script                                |
| `.env`          | Stores your API key (excluded from Git)           |
| `.gitignore`    | Prevents sensitive files from being tracked       |
| `requirements.txt` | Python dependencies                          |
| `README.md`     | Complete project guide (this file)                |

---

## 📄 requirements.txt

```txt
google-generativeai
python-dotenv
```

---

## 🛑 .gitignore

```gitignore
.env
__pycache__/
*.pyc
venv/
.DS_Store
```

---

## 📌 TODO (Future Enhancements)

- GUI with Tkinter or Streamlit
- Save chat history to file
- Add voice input/output
- Memory for multi-turn conversation
- Secure secrets using vaults
