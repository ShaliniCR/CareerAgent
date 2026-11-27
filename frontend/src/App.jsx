import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import "./App.css";

const API_URL = (import.meta.env.VITE_API_URL || "http://localhost:8000").replace(/\/$/, "");
const THREAD_KEY = "careerbuddy_thread_id";

const SUGGESTIONS = [
  "What do I need to become an ML engineer?",
  "I know Python and SQL, which path suits me?",
  "I'm a backend developer. How do I move into AI?",
];

async function api(path, options) {
  let res;
  try {
    res = await fetch(`${API_URL}${path}`, {
      headers: { "Content-Type": "application/json" },
      ...options,
    });
  } catch {
    throw new Error("Can't reach the CareerBuddy server. Check that the backend is running and try again.");
  }
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || `Server error (${res.status}).`);
  }
  return res.json();
}

export default function App() {
  const [threadId, setThreadId] = useState(() => localStorage.getItem(THREAD_KEY));
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [thinking, setThinking] = useState(false);
  const [loadingHistory, setLoadingHistory] = useState(false);
  const [error, setError] = useState("");
  const bottomRef = useRef(null);

  // On first load: restore the saved conversation, or start a new one.
  useEffect(() => {
    const saved = localStorage.getItem(THREAD_KEY);
    if (saved) {
      setLoadingHistory(true);
      api(`/history/${encodeURIComponent(saved)}`)
        .then(setMessages)
        .catch((e) => setError(e.message))
        .finally(() => setLoadingHistory(false));
    } else {
      startNewChat();
    }
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, thinking]);

  async function startNewChat() {
    setError("");
    try {
      const { thread_id } = await api("/new-chat", { method: "POST" });
      localStorage.setItem(THREAD_KEY, thread_id);
      setThreadId(thread_id);
      setMessages([]);
      return thread_id;
    } catch (e) {
      setError(e.message);
      return null;
    }
  }

  async function send(text) {
    const message = (text ?? input).trim();
    if (!message || thinking) return;
    setError("");
    let tid = threadId || (await startNewChat());
    if (!tid) return;
    setInput("");
    setMessages((m) => [...m, { role: "user", content: message }]);
    setThinking(true);
    try {
      const { reply } = await api("/chat", {
        method: "POST",
        body: JSON.stringify({ thread_id: tid, message }),
      });
      setMessages((m) => [...m, { role: "assistant", content: reply }]);
    } catch (e) {
      setError(e.message);
    } finally {
      setThinking(false);
    }
  }

  function onKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  }

  const empty = messages.length === 0 && !loadingHistory;

  return (
    <div className="app">
      <header className="header">
        <div className="brand">
          <span className="logo" aria-hidden="true">CB</span>
          <div>
            <h1>CareerBuddy</h1>
            <p>Your career coach for Data Science, AI and ML</p>
          </div>
        </div>
        <button className="new-chat" onClick={startNewChat} disabled={thinking}>
          + New chat
        </button>
      </header>

      <main className="messages">
        {loadingHistory && <div className="status">Loading your conversation...</div>}
        {empty && (
          <div className="welcome">
            <h2>Hi, I'm CareerBuddy 👋</h2>
            <p>
              Tell me about your background and what you enjoy, and I'll help you pick a path:
              Data Scientist, ML Engineer, AI Engineer or MLOps Engineer.
            </p>
            <div className="suggestions">
              {SUGGESTIONS.map((s) => (
                <button key={s} onClick={() => send(s)} disabled={thinking}>
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}
        {messages.map((m, i) => (
          <div key={i} className={`msg ${m.role}`}>
            <div className="bubble">
              {m.role === "assistant" ? <ReactMarkdown>{m.content}</ReactMarkdown> : m.content}
            </div>
          </div>
        ))}
        {thinking && (
          <div className="msg assistant">
            <div className="bubble thinking">
              Thinking<span className="dots"><span>.</span><span>.</span><span>.</span></span>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </main>

      {error && (
        <div className="error" role="alert">
          {error}
          <button onClick={() => setError("")} aria-label="Dismiss">×</button>
        </div>
      )}

      <footer className="composer">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder="Ask about a career path, skills, or next steps..."
          rows={1}
          disabled={thinking}
        />
        <button onClick={() => send()} disabled={thinking || !input.trim()}>
          Send
        </button>
      </footer>
    </div>
  );
}
