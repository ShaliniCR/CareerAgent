# CareerBuddy

An AI career coach for Data Science, AI and ML, with persistent memory.

- `backend/`: FastAPI, LangChain `create_agent` with `claude-haiku-5-5`, the `search_career_paths` tool over `career_paths.md`, and `SqliteSaver` memory in `memory.db`
- `frontend/`: React (Vite) chat UI. It keeps `thread_id` in localStorage and restores the chat through `GET /history/{thread_id}`

## Run locally

```bash
# Backend
cd backend
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python -r requirements.txt
cp .env.example .env   # then set ANTHROPIC_API_KEY
.venv/bin/uvicorn main:app --port 8000

# Frontend (in a second terminal)
cd frontend
npm install
cp .env.example .env   # VITE_API_URL=http://localhost:8000
npm run dev            # http://localhost:5173
```

## Deploy

- **Backend (Render or Railway):** start command `uvicorn main:app --host 0.0.0.0 --port $PORT`. Set these environment variables:
  - `ANTHROPIC_API_KEY`
  - `FRONTEND_ORIGINS=https://<your-frontend-domain>`
  - `MEMORY_DB_PATH=/data/memory.db`, with a persistent disk or volume mounted at `/data`
- **Frontend (Vercel or Netlify):** root directory `frontend`, build command `npm run build`, output directory `dist`. Set the environment variable `VITE_API_URL=https://<your-backend-domain>`.
