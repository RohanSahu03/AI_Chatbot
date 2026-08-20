def load_document(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def retrieve(document, query):

    stopwords = {
        "what", "is", "the", "a", "an",
        "how", "many", "do", "does",
        "of", "to", "for", "in", "on",
        "are", "can", "i", "we", "you",
        "they", "their", "me", "get"
    }

    query_words = [
        word.lower().strip(".,?!")
        for word in query.split()
        if word.lower().strip(".,?!") not in stopwords
    ]

    sentences = [
        sentence.strip()
        for sentence in document.split("\n")
        if sentence.strip()
    ]

    scored_sentences = []

    for sentence in sentences:

        sentence_lower = sentence.lower()

        score = 0

        for word in query_words:
            if word in sentence_lower:
                score += 1

        if score > 0:
            scored_sentences.append((score, sentence))

    scored_sentences.sort(reverse=True)

    return [sentence for score, sentence in scored_sentences]


document = load_document("data/company_info.txt")

query = "How many days of paid leave do employees receive?"

results = retrieve(document, query)

print(results)