"""CareerBuddy agent: LangChain create_agent + Claude Haiku 5.5 + SqliteSaver memory."""

import os
import re
import sqlite3
from pathlib import Path

from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langgraph.checkpoint.sqlite import SqliteSaver

BASE_DIR = Path(__file__).parent
KNOWLEDGE_FILE = BASE_DIR / "career_paths.md"
MEMORY_DB_PATH = os.getenv("MEMORY_DB_PATH", str(BASE_DIR / "memory.db"))

STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "on", "for", "is", "are", "i",
    "me", "my", "do", "does", "what", "which", "how", "need", "become", "be", "with",
    "it", "as", "at", "can", "you", "know", "want", "should", "about", "from", "that",
    "this", "am", "have", "has", "get", "into", "path", "career",
}


def _load_sections() -> list[dict]:
    """Split the knowledge file into one section per '## ' heading."""
    text = KNOWLEDGE_FILE.read_text(encoding="utf-8")
    sections = []
    for chunk in re.split(r"^## ", text, flags=re.MULTILINE)[1:]:
        title, _, body = chunk.partition("\n")
        kw = re.search(r"\*\*Keywords:\*\*(.*)", body)
        sections.append({
            "title": title.strip(),
            "content": f"## {chunk.strip()}",
            "keywords": kw.group(1).lower() if kw else "",
        })
    return sections


SECTIONS = _load_sections()


def _tokens(s: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9/+#-]+", s.lower()) if t not in STOPWORDS and len(t) > 1]


def _score(query: str, section: dict) -> float:
    q_tokens = _tokens(query)
    if not q_tokens:
        return 0.0
    q_text = " ".join(q_tokens)
    title = section["title"].lower()
    body = section["content"].lower()
    score = 0.0
    # Keyword phrases matched in the query count most (per the KB's agent notes).
    for phrase in (p.strip() for p in section["keywords"].rstrip(".").split(",")):
        if phrase and phrase in q_text:
            score += 5 * len(phrase.split())
    for t in set(q_tokens):
        if t in title:
            score += 4
        if t in section["keywords"]:
            score += 2
        score += min(body.count(t), 5) * 0.5
    return score


@tool
def search_career_paths(query: str) -> str:
    """Search the CareerBuddy knowledge base of Data Science, AI and ML career paths
    (Data Scientist, Machine Learning Engineer, AI Engineer, MLOps Engineer, plus
    guidance on choosing and switching paths). Returns the best-matching sections.
    Use this before giving any career advice.

    Args:
        query: The user's question or the skills/background/role to look up.
    """
    ranked = sorted(SECTIONS, key=lambda s: _score(query, s), reverse=True)
    top = [s for s in ranked[:2] if _score(query, s) > 0]
    if not top:
        top = [s for s in SECTIONS if s["title"] in ("At a glance", "Choosing a path")]
    return "\n\n---\n\n".join(s["content"] for s in top)


SYSTEM_PROMPT = """You are CareerBuddy, a friendly, practical career coach for people moving into Data Science, AI and ML.

Knowledge source: always call the `search_career_paths` tool before giving career advice, and base your advice on what it returns, not on general knowledge alone. Search again if the user's question moves to a different path or topic. When you rely on the knowledge base, use its terms (path names, skill areas, first steps) so the user can see where the advice comes from.

How to coach:
1. If you don't yet know the user's background (education, current role, skills they have) and what kind of work they enjoy, ask about it briefly before recommending a path. Ask at most two short questions at a time.
2. Once you know their background, recommend ONE primary path, with reasons tied to their background and interests. You may mention one alternative briefly.
3. List the mandatory skills for that path they already have, and the ones they still need.
4. Suggest two or three concrete next steps taken from that path's First steps.
5. Remember what the user told you earlier in the conversation and build on it; don't ask again for things they already said.

Scope: stay on career topics (careers, skills, learning plans, roles, job searching in Data Science, AI and ML). If asked about something unrelated, politely say you can only help with career questions and steer back.

Style: clear and encouraging, concise, using short headings or bullet lists where helpful. Treat skill lists as typical expectations, not fixed rules."""


_conn = sqlite3.connect(MEMORY_DB_PATH, check_same_thread=False)
checkpointer = SqliteSaver(_conn)
checkpointer.setup()

model = ChatAnthropic(model="claude-haiku-5-5", max_tokens=4096)

agent = create_agent(
    model=model,
    tools=[search_career_paths],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)
