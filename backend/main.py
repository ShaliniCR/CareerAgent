"""CareerBuddy FastAPI backend."""

import os
import uuid

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from langchain_core.messages import AIMessage, HumanMessage  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from agent import agent  # noqa: E402

app = FastAPI(title="CareerBuddy API")

origins = [o.strip() for o in os.getenv(
    "FRONTEND_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
).split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    thread_id: str
    message: str


def _config(thread_id: str) -> dict:
    return {"configurable": {"thread_id": thread_id}}


@app.get("/")
def health():
    return {"status": "ok", "service": "CareerBuddy"}


@app.post("/new-chat")
def new_chat():
    return {"thread_id": str(uuid.uuid4())}


@app.post("/chat")
def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message must not be empty.")
    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": req.message}]},
            config=_config(req.thread_id),
        )
    except Exception as e:  # surface upstream failures as a clean 502
        raise HTTPException(status_code=502, detail=f"Agent error: {e}") from e
    last = result["messages"][-1]
    reply = last.text if isinstance(last, AIMessage) else str(last.content)
    return {"reply": reply or "Sorry, I couldn't come up with a reply. Please try again."}


@app.get("/history/{thread_id}")
def history(thread_id: str):
    state = agent.get_state(_config(thread_id))
    messages = state.values.get("messages", []) if state and state.values else []
    out = []
    for m in messages:
        if isinstance(m, HumanMessage):
            out.append({"role": "user", "content": m.text})
        elif isinstance(m, AIMessage) and m.text.strip():
            # Skip tool-call-only steps; keep the agent's actual replies.
            out.append({"role": "assistant", "content": m.text})
    return out
