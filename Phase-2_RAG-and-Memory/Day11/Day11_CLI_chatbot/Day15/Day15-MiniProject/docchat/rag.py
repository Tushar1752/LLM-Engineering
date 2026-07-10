"""
docchat/rag.py - the "R-A-G" glue: Retrieve, Augment, then let the LLM Generate.

This module takes the retrieved chunks and a question and builds the exact
`messages` list we send to Groq. It is the step that "augments" the user's
question with context so the model answers from the documents, not from its
general training.

It does NOT call the LLM itself (that's llm.py) and does NOT do retrieval
(that's vector_store.py). It only assembles the prompt - one job.
"""

from config import SYSTEM_PROMPT
def build_context_block(matches: list) -> str:
    """Format retrieved chunks into a numbered, cited context block."""
    if not matches:
        return "(no documents retrieved)"
    lines = []
    for i, match in enumerate(matches, start=1):
      
        lines.append(
            f"[Source {i} | file: {match['source']} | "
            f"relevance: {match['similarity']:.2f}]\n{match['document']}"
        )
    return "\n\n".join(lines)

def build_messages(question: str, matches: list, history: list) -> list:
    """Assemble the messages list for Groq: system + past turns + grounded question.

    `history` is the running chat (a list of {"role","content"} dicts, minus the
    current question) so the bot can follow up on earlier turns.
    """
    context_block = build_context_block(matches)
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({
        "role": "user",
        "content": (
            f"Context from the user's documents:\n{context_block}\n\n"
            f"Question: {question}"
        ),
    })
    return messages

if __name__ == "__main__":
    fake_matches = [
        {"document": "Refunds take 5 business days.", "source": "faq.txt", "similarity": 0.81},
        {"document": "Support is open Mon-Fri.", "source": "faq.txt", "similarity": 0.44},
    ]
    msgs = build_messages("How long for a refund?", fake_matches, history=[])
    for m in msgs:
        print(f"--- {m['role']} ---")
        print(m["content"])
        print()