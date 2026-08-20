import chromadb
import ollama


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="company_info"
)


query = "How much vacation time do employees get?"


response = ollama.embed(
    model="nomic-embed-text",
    input=query
)

query_embedding = response["embeddings"][0]


results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)


print("\nRelevant information:\n")

for document in results["documents"][0]:

    print(document)
    print()