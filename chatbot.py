import ollama

print("Welcome to AI Chatbot!")
print("Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("AI:", response["message"]["content"])