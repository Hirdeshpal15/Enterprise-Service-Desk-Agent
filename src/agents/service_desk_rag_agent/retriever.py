from pathlib import Path

from chunker import DocumentChunker


class PolicyRetriever:
    def __init__(self, knowledge_dir: Path):
        self.chunker = DocumentChunker()
        self.chunks = self.chunker.load_chunks(knowledge_dir)

    def retrieve(self, question: str):
        question_words = question.lower().split()

        best_score = -1
        best_chunk = None

        for chunk in self.chunks:

            score = sum(
                1
                for word in question_words
                if word in chunk["content"].lower()
            )

            if score > best_score:
                best_score = score
                best_chunk = chunk

        return {
            "document": best_chunk["document"],
            "chunk_id": best_chunk["chunk_id"],
            "score": best_score,
            "content": best_chunk["content"],
        }