import os

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity


DATA_FOLDER = "data"


class KnowledgeBase:

    def __init__(self):

        self.documents = []

        self.file_names = []

        self.load()

    def load(self):

        self.documents.clear()

        self.file_names.clear()

        if not os.path.exists(DATA_FOLDER):

            os.makedirs(DATA_FOLDER)

        for file in os.listdir(DATA_FOLDER):

            if file.endswith(".txt"):

                path = os.path.join(DATA_FOLDER, file)

                with open(path, encoding="utf-8") as f:

                    self.documents.append(f.read())

                    self.file_names.append(file)

    def search(self, query, top_k=5):

    if not self.documents:
        return "", []

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1,3),
        max_features=5000
    )

    vectors = vectorizer.fit_transform(
        self.documents + [query]
    )

    scores = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )[0]

    ranked = scores.argsort()[::-1]

    context = []

    files = []

    for i in ranked:

        if scores[i] > 0.02:

            context.append(self.documents[i])

            files.append(self.file_names[i])

        if len(context) >= top_k:

            break

    return "\n\n".join(context), files
