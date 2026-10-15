"""Interactive Security+ study assistant backed by a Qdrant vector store.

Retrieves the most relevant chunks from the indexed study guide, then asks
the model to answer using only that context and to cite page numbers.
Run index.py first to build the collection.
"""

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

QDRANT_URL = "http://localhost:6333"
COLLECTION = "learning_rag"
MODEL = "gpt-5"

SYSTEM_TEMPLATE = """You are a study assistant helping students prepare for the CompTIA Security+ exam.

Rules:
- Answer ONLY from the context below. If the context does not contain the answer, say so.
- Always tell the user which page number(s) to open to read more.
- Where helpful, finish with one or two practice questions based on the context.

Context:
{context}
"""

client = OpenAI()
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
vector_db = QdrantVectorStore.from_existing_collection(
    url=QDRANT_URL,
    collection_name=COLLECTION,
    embedding=embedding_model,
)


def build_context(query: str) -> str:
    results = vector_db.similarity_search(query=query, k=4)
    return "\n\n".join(
        f"Page {doc.metadata.get('page_label', '?')}:\n{doc.page_content}"
        for doc in results
    )


def main() -> None:
    print("Security+ study assistant. Type 'exit' to quit.")
    while True:
        query = input("\nAsk a question: ").strip()
        if query.lower() in {"exit", "quit"}:
            break
        if not query:
            continue

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_TEMPLATE.format(context=build_context(query))},
                {"role": "user", "content": query},
            ],
        )
        print(f"\n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
