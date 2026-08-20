def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def split_into_chunks(document):
    chunks = document.split("\n\n")

    return [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]

document = load_document("data/company_info.txt")

chunks = split_into_chunks(document)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i}:")
    print(chunk)