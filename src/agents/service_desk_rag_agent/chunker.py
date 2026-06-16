from pathlib import Path


class DocumentChunker:
    def __init__(self, chunk_size=300):
        self.chunk_size = chunk_size

    def chunk_document(self, text: str):
        chunks = []

        for i in range(0, len(text), self.chunk_size):
            chunk = text[i:i + self.chunk_size]
            chunks.append(chunk)

        return chunks

    def load_chunks(self, knowledge_dir: Path):
        all_chunks = []

        for file in knowledge_dir.glob("*.md"):
            content = file.read_text()

            chunks = self.chunk_document(content)

            for index, chunk in enumerate(chunks):
                all_chunks.append(
                    {
                        "document": file.name,
                        "chunk_id": index,
                        "content": chunk,
                    }
                )

        return all_chunks