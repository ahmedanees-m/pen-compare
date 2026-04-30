"""Build ChromaDB RAG index from all repo text documents.

Indexes: .md, .yaml, .yml, .json, .txt under /workspace/pen-compare
(config/, prereg/, results/, docs/, pen_compare/ source files).
ChromaDB stored at data/rag_db/ (bind-mounted, persists across container runs).
"""

from pathlib import Path

from pen_compare.rag.qa import PenStackQA

REPO_ROOT = Path("/workspace/pen-compare")
DB_PATH = REPO_ROOT / "data" / "rag_db"

print(f"Building RAG index from {REPO_ROOT}")
qa = PenStackQA(db_path=DB_PATH)
n = qa.build_index(REPO_ROOT)
print(f"Indexed {n} chunks -> ChromaDB at {DB_PATH}")
print(f"Collection size: {qa.collection_count()} vectors")

# Sanity check: ask a gate-definition question
q = "What is the G1 DSB Avoidance gate threshold?"
print(f"\nSanity Q: {q}")
print(f"A: {qa.ask(q)}")
