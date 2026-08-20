import ollama

print("Welcome to AI Chatbot!")
print("Type 'exit' to quit.")

messages = []

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
        messages=messages
    )

    ai_response = response["message"]["content"]

    print("AI:", ai_response)

    messages.append({
        "role": "assistant",
        "content": ai_response
    })