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

    def search(self, query, top_k=3):

        if len(self.documents) == 0:

            return "", []

        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )

        vectors = vectorizer.fit_transform(
            self.documents + [query]
        )

        scores = cosine_similarity(
            vectors[-1],
            vectors[:-1]
        )[0]

        ranked = scores.argsort()[::-1]

        selected = []

        files = []

        for i in ranked[:top_k]:

            if scores[i] > 0.03:

                selected.append(self.documents[i])

                files.append(self.file_names[i])

        return "\n\n".join(selected), files
