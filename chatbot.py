import ollama

print("Welcome to AI Chatbot!")
print("Type 'exit' to quit.")

messages = [
    {
        "role": "system",
        "content": """
        You are a helpful AI assistant.

        Explain concepts clearly and simply.
        Assume the user may be a beginner.

        When explaining technical topics, provide
        examples when useful.

        If you are unsure about something, say so
        rather than making up information.
        """
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="gemma3:4b",
        messages=messages,
        stream=True
    )

    ai_response = ""

    print("AI: ", end="")

    for chunk in response:
        text = chunk["message"]["content"]

        print(text, end="", flush=True)

        ai_response += text

    print()

    messages.append({
        "role": "assistant",
        "content": ai_response
    })