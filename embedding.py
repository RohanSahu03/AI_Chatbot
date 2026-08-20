import ollama
import numpy as np


texts = [
    "Employees receive 20 days of paid leave every year.",
    "How much vacation time do employees get?",
    "The company provides health insurance to employees."
]


response = ollama.embed(
    model="nomic-embed-text",
    input=texts
)

embeddings = response["embeddings"]


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


similarity_1_2 = cosine_similarity(
    embeddings[0],
    embeddings[1]
)

similarity_1_3 = cosine_similarity(
    embeddings[0],
    embeddings[2]
)


print("Similarity between leave and vacation:")
print(similarity_1_2)

print("\nSimilarity between leave and health insurance:")
print(similarity_1_3)