from pathlib import Path

text = Path(
    "knowledge_base/software_request_policy.md"
).read_text()

chunk_size = 200

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 40)
    print(chunk)