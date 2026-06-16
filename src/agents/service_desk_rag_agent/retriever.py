from pathlib import Path


class PolicyRetriever:
    def __init__(self, knowledge_dir: Path):
        self.knowledge_dir = knowledge_dir
        self.documents = self._load_documents()

    def _load_documents(self):
        documents = {}

        for file in self.knowledge_dir.glob("*.md"):
            documents[file.name] = file.read_text()

        return documents

    def retrieve(self, question: str):
        question_words = question.lower().split()

        best_score = -1
        best_document = None
        best_content = ""

        for filename, content in self.documents.items():
            score = sum(
                1 for word in question_words
                if word in content.lower()
            )

            if score > best_score:
                best_score = score
                best_document = filename
                best_content = content

        return {
            "document": best_document,
            "score": best_score,
            "content": best_content
        }