import ollama
import chromadb


# -----------------------------
# Connect to ChromaDB
# -----------------------------

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="company_info"
)


# -----------------------------
# Search relevant information
# -----------------------------

def retrieve_context(query):

    response = ollama.embed(
        model="nomic-embed-text",
        input=query
    )

    query_embedding = response["embeddings"][0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results["documents"][0]

    return "\n\n".join(documents)


# -----------------------------
# Ask Gemma
# -----------------------------

def ask_llm(question, context):

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using the provided context.

If the answer cannot be found in the context,
say that you don't have enough information.

Do not make up information.

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )

    answer = ""

    print("\nAI: ", end="")

    for chunk in response:

        text = chunk["message"]["content"]

        print(text, end="", flush=True)

        answer += text

    print()

    return answer


# -----------------------------
# Chat loop
# -----------------------------

print("RAG Chatbot")
print("Ask questions about TechCorp.")
print("Type 'exit' to quit.")

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    context = retrieve_context(question)

    ask_llm(question, context)