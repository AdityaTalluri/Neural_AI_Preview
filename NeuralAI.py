import google.generativeai as genai


API_KEY = "AIzaSyD1Ul9w5hzeNFQSN3l3fbZTlXAtnBeqlaY"
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
