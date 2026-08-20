import chromadb
import ollama

from document_processor import load_document, split_into_chunks


# Create Chroma client
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# Create collection
collection = client.get_or_create_collection(
    name="company_info"
)


# Load document
document = load_document("data/company_info.txt")

# Split document into chunks
chunks = split_into_chunks(document)


# Create embeddings
response = ollama.embed(
    model="nomic-embed-text",
    input=chunks
)

embeddings = response["embeddings"]


# Store chunks and embeddings
for i, (chunk, embedding) in enumerate(
    zip(chunks, embeddings)
):

    collection.upsert(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding]
    )


print("Documents stored successfully!")

print(
    "Number of documents:",
    collection.count()
)