# MathIntel — Project Structure & Initial Codebase Guide

This file defines a **clean project structure** and a **starter codebase plan** for an AI tool to build against.  
Use this as a blueprint for scaffolding, refactors, or automated generation.

---

## 📁 Target Repository Structure

```
mathintel/
├── README.md
├── guide.md
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── health.py
│   │   │   │   ├── solve.py
│   │   │   │   ├── auth.py
│   │   │   │   └── notebook.py
│   │   │   └── deps.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── logging.py
│   │   ├── services/
│   │   │   ├── math_engine.py
│   │   │   ├── socratic_tutor.py
│   │   │   ├── llm_client.py
│   │   │   ├── vector_store.py
│   │   │   └── ocr_pipeline.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── session.py
│   │   │   └── notebook.py
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   ├── solve.py
│   │   │   └── notebook.py
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   └── base.py
│   │   └── utils/
│   │       ├── latex.py
│   │       └── prompts.py
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── MathEditor.tsx
│   │   │   ├── ChatPanel.tsx
│   │   │   ├── Notebook.tsx
│   │   │   ├── Visualizer.tsx
│   │   │   └── KnowledgeMap.tsx
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Session.tsx
│   │   │   └── Profile.tsx
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   └── auth.ts
│   │   ├── styles/
│   │   └── App.tsx
│   ├── public/
│   └── Dockerfile
├── docker-compose.yml
└── .env.example
```

---

## ✅ Backend Initial Codebase Plan (FastAPI)

### `main.py`
- Initialize FastAPI
- Include routers: `/health`, `/solve`, `/auth`, `/notebook`
- Enable CORS

### API Endpoints (MVP)
- `GET /health` → basic health check
- `POST /solve` → accepts math problem + context  
- `POST /auth/register` → create user  
- `POST /auth/login` → JWT auth  
- `GET /notebook/:id` → fetch saved session  
- `POST /notebook` → save current conversation

### Core Services

#### `MathEngine`
- Uses SymPy
- Methods:
  - `solve_algebra()`
  - `differentiate()`
  - `integrate()`
  - `linear_algebra()`
- Returns structured output:  
  `{ latex, steps, result, explanation }`

#### `SocraticTutor`
- LLM‑powered dialog manager
- Inputs: user msg + history  
- Outputs: question + hint + next micro‑task  
- NEVER returns final answer first.

#### `LLMClient`
- Abstracted model client  
- Supports GPT‑4 / Claude / Gemini  
- Handles prompt formatting, retries, and guardrails

#### `VectorStore`
- ChromaDB integration  
- Store embeddings of solved problems  
- Retrieve similar examples for scaffolding

#### `OCRPipeline`
- Pix2Tex / Vision API  
- Convert images → LaTeX → send to MathEngine

---

## ✅ Frontend Initial Codebase Plan (React)

### Core Components
- **MathEditor** → LaTeX input
- **ChatPanel** → Socratic tutoring chat
- **Notebook** → saved sessions + history
- **Visualizer** → plots / derivations
- **KnowledgeMap** → concept graph

### UI Flow
1. User enters question / uploads image  
2. `/solve` returns Socratic response  
3. Chat displays hints + questions  
4. Notebook saves session

---

## ✅ Minimal AI Workflow Contract

The AI tool should use this JSON‑like contract:

```
Input:
{
  "problem": "string",
  "context": "string",
  "history": [ { "role": "user/assistant", "content": "..." } ]
}

Output:
{
  "next_question": "string",
  "hint": "string",
  "step": "string",
  "latex": "string",
  "tags": ["calculus", "chain rule"],
  "confidence": 0.0
}
```

---

## ✅ Initial Development Order (Suggested)

1. Setup backend skeleton + `/health`
2. Implement `MathEngine` with SymPy
3. Add `/solve` endpoint
4. Add Socratic prompting + LLM client
5. Build minimal React UI
6. Persist sessions + auth
7. Add OCR pipeline
8. Add embeddings + knowledge tracking

---

## ✅ Environment Variables (`.env.example`)

```
OPENAI_API_KEY=
DATABASE_URL=
REDIS_URL=
CHROMA_URL=
JWT_SECRET=
UPLOAD_DIR=./uploads
```

---

## ✅ Tooling & Deployment

- **Docker Compose**: backend + frontend + postgres + redis
- **CI/CD**: GitHub Actions (lint/test/deploy)
- **Hosting**: Railway / Render / Fly.io

---

## ✅ Final Goal

A complete, deployable AI tutor that:
- teaches ML math Socratically
- tracks student understanding
- supports multi‑modal input
- scales into a full learning platform