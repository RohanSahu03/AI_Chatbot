import ollama
import numpy as np

from document_processor import load_document, split_into_chunks


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


document = load_document("data/company_info.txt")

chunks = split_into_chunks(document)

response = ollama.embed(
    model="nomic-embed-text",
    input=chunks
)

embeddings = response["embeddings"]


query = "How much vacation time do employees get?"

query_response = ollama.embed(
    model="nomic-embed-text",
    input=query
)

query_embedding = query_response["embeddings"][0]


results = []

for chunk, embedding in zip(chunks, embeddings):

    similarity = cosine_similarity(
        query_embedding,
        embedding
    )

    results.append((similarity, chunk))


results.sort(reverse=True)


print("\nMost relevant chunks:\n")

for similarity, chunk in results[:3]:

    print("Similarity:", similarity)
    print("Chunk:", chunk)
    print()