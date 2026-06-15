documents = [
    "Employees may request software through the IT Service Portal.",
    "VPN access requires MFA and manager approval.",
    "Passwords must contain at least 12 characters.",
    "Access requests require manager and application owner approval."
]

query = "How do I install Adobe Acrobat?"

print("Question:")
print(query)

print("\nDocuments:")
for i, doc in enumerate(documents, start=1):
    print(f"{i}. {doc}")

print("\nConcept:")

print("""
Keyword Search looks for exact words.

Question:
    install Adobe Acrobat

Document:
    request software through IT Service Portal

Keyword overlap:
    almost none

Result:
    may miss the correct document


Vector Search uses meaning instead of exact words.

install Adobe Acrobat
        ≈
request software

Therefore the software policy document
would be ranked as the most relevant result.
""")