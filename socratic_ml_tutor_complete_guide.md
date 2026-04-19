# Socratic ML Math Tutor — Complete Project Reference Guide
> **Author:** Built from Vishruth's conversations with Claude  
> **Last updated:** April 2026  
> **Purpose:** Master reference document — everything about this project in one place

---

## Table of Contents

1. [Project Identity — What This Is and Why It Exists](#1-project-identity)
2. [Why This Is Unique — The Honest Analysis](#2-why-this-is-unique)
3. [Complete Tech Stack with Google Integration](#3-complete-tech-stack)
4. [Full System Architecture](#4-full-system-architecture)
5. [Phase 0 — Environment Setup](#phase-0--environment-setup)
6. [Phase 1 — Python Core](#phase-1--python-core)
7. [Phase 2 — FastAPI Backend](#phase-2--fastapi-backend)
8. [Phase 3 — Math Engine with SymPy](#phase-3--math-engine-with-sympy)
9. [Phase 4 — The Socratic AI Brain](#phase-4--the-socratic-ai-brain)
10. [Phase 5 — Database and Authentication](#phase-5--database-and-authentication)
11. [Phase 6 — React Frontend](#phase-6--react-frontend)
12. [Phase 7 — Knowledge Tracking with Embeddings](#phase-7--knowledge-tracking-with-embeddings)
13. [Phase 8 — Vision Pipeline and Deployment](#phase-8--vision-pipeline-and-deployment)
14. [Book Chapter Map — Hands-On ML with Keras](#14-book-chapter-map)
15. [Google Services Setup Guide](#15-google-services-setup-guide)
16. [Daily Workflow](#16-daily-workflow)
17. [Complete Folder Structure](#17-complete-folder-structure)
18. [Resume Bullet Points](#18-resume-bullet-points)
19. [Quick Reference — Commands Cheat Sheet](#19-quick-reference--commands-cheat-sheet)

---

## 1. Project Identity

### What you are building
**Name:** Socratic ML Math Tutor  
**Tagline:** "You use gradient descent every day. But do you actually know why it works?"

A web application that teaches the **mathematics behind machine learning** through the Socratic method — it never gives answers directly. It asks guiding questions until you discover the answer yourself.

### The core philosophy (the one idea the entire project is built on)
Every other tool (Wolfram Alpha, ChatGPT, Symbolab, Photomath) does the same thing: it **answers** your question. You get the fish, you never learn to fish.

This project does the opposite. When you type "what is backpropagation?", instead of defining it, the tutor asks: *"Before we get there — what do you think the word 'back' refers to in backpropagation?"*

You earn the answer through reasoning. That is the difference.

### Who it is for
- Data scientists and ML engineers who use tools (gradient descent, backprop, attention) without understanding the underlying mathematics
- ML students working through textbooks who want a thinking partner, not an answer machine
- Anyone learning machine learning who wants to genuinely understand, not just implement

### Why this has no direct competition
- Wolfram Alpha: solves problems, no teaching
- Photomath: reads and solves, no teaching
- ChatGPT/Claude/Gemini: explains if you ask, but will always just answer directly
- NotebookLM: great for document chat, not mathematics-specific, not Socratic
- Symbolab: step-by-step solutions, still just gives answers

**The gap:** No tool exists that combines (1) exact mathematical computation, (2) Socratic dialogue that forces the student to think, (3) tracking of what the student actually understands vs. just guesses, (4) focus specifically on ML mathematics.

---

## 2. Why This Is Unique — The Honest Analysis

### What already exists (do not rebuild these)
| Tool | What it does | Why you are not competing with it |
|------|-------------|----------------------------------|
| Wolfram Alpha | Solves from basic to PhD, shows steps | 25 years old, massive knowledge base |
| Photomath | Camera → solution, step-by-step | 220M+ downloads, mobile-first |
| Symbolab | Step-by-step, topic-specific | Widely adopted in schools |
| ChatGPT/Claude | Solve, explain, remember context | Trillion dollar companies behind them |
| NotebookLM | Chat with documents | Google's product, excellent |

### What nobody has built well
1. **Diagnose WHY you got it wrong** — not just that you got it wrong
2. **Guide you instead of answering** — Socratic AI that asks questions
3. **Connect math across fields** — show same concept in physics, CS, economics simultaneously
4. **Track your knowledge map** — know exactly which concepts you understand vs. misunderstand
5. **ML math specifically** — practitioners who code ML but don't understand the math underneath
6. **Proof verification for learners** — student writes a proof, AI checks logical validity line by line
7. **Math intuition, not just answers** — why does this formula exist?

### The two directions combined
**Direction 1 (Socratic Tutor):** Asks questions instead of answering. Detects misconceptions. You earn the answer.

**Direction 3 (ML Math Explainer):** Paste ML code or a paper formula. Get first-principles derivation + interactive quizzing.

**Combined:** A Socratic tutor specifically for the math behind machine learning. This intersection is completely unoccupied.

---

## 3. Complete Tech Stack with Google Integration

### Backend
| Layer | Tool | Why |
|-------|------|-----|
| Web framework | FastAPI (Python) | Fast, auto-generates API docs, async support |
| Math computation | SymPy | Exact symbolic answers, not approximations |
| AI/LLM | Gemini 2.0 Flash (Google AI Studio) | Free tier: 1500 requests/day, excellent quality |
| Embeddings | Gemini text-embedding-004 | Free, replaces OpenAI embeddings |
| Vector database | ChromaDB | Store and search concept embeddings |
| Database | PostgreSQL | Store users, sessions, messages |
| ORM | SQLAlchemy | Python classes ↔ database tables |
| Cache | Redis | Session memory, conversation context |
| Auth verification | firebase-admin | Verify Firebase tokens on backend |
| File storage | Google Cloud Storage | Store uploaded math images |
| OCR | Pix2Tex + GPT-4o Vision | Extract LaTeX from math photos |
| Server | Uvicorn | Runs FastAPI |

### Frontend
| Layer | Tool | Why |
|-------|------|-----|
| Framework | React | Component-based, industry standard |
| Math rendering | KaTeX (react-katex) | Renders LaTeX beautifully in browser |
| Auth | Firebase Auth SDK | Google Sign-In in 5 lines of code |
| HTTP calls | axios | Cleaner than fetch() for API calls |
| Routing | React Router | Multiple pages without page reload |

### Infrastructure (All Google, all free at learning scale)
| Service | Google Tool | Free tier |
|---------|------------|-----------|
| Authentication | Firebase Auth | 10,000 users/month |
| File uploads | Google Cloud Storage | 5GB forever |
| Backend hosting | Cloud Run | 2 million requests/month |
| Frontend hosting | Firebase Hosting | 10GB/month |
| Learning sandbox | Google Colab | Free GPU, runs in browser |
| LLM + Embeddings | Google AI Studio | 1500 requests/day free |

### What this means for cost
**Total monthly cost to build and run at portfolio/learning scale: ₹0**

---

## 4. Full System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  FRONTEND (React)                   │
│  ┌────────────┐ ┌──────────┐ ┌───────┐ ┌────────┐  │
│  │ Math Editor│ │Socratic  │ │Upload │ │Knowledge│  │
│  │KaTeX input │ │Chat UI   │ │Image  │ │  Map   │  │
│  └────────────┘ └──────────┘ └───────┘ └────────┘  │
└────────────────────────┬────────────────────────────┘
                         │ REST API + Firebase Token
                         ▼
┌─────────────────────────────────────────────────────┐
│                BACKEND (FastAPI)                     │
│  ┌────────────┐ ┌──────────┐ ┌───────┐ ┌────────┐  │
│  │API Gateway │ │Socratic  │ │Vision │ │Session │  │
│  │Auth verify │ │Engine    │ │OCR    │ │  API   │  │
│  └────────────┘ └──────────┘ └───────┘ └────────┘  │
└────────────────────────┬────────────────────────────┘
                         │
            ┌────────────┴────────────┐
            ▼                         ▼
┌─────────────────┐       ┌──────────────────────┐
│    AI LAYER     │       │      DATA LAYER       │
│                 │       │                       │
│ Gemini 2.0 Flash│       │ PostgreSQL             │
│ (reasoning)     │       │ (users, sessions)     │
│                 │       │                       │
│ SymPy           │       │ Redis                 │
│ (exact math)    │       │ (session cache)       │
│                 │       │                       │
│ Gemini Embeddings│       │ ChromaDB              │
│ (concept vectors)│       │ (knowledge vectors)   │
│                 │       │                       │
│ Pix2Tex         │       │ Cloud Storage         │
│ (math OCR)      │       │ (uploaded images)     │
└─────────────────┘       └──────────────────────┘
```

### How a single interaction flows
```
1. User types: "I think gradient descent always finds the global minimum"
2. Firebase token verified by FastAPI
3. Gemini detects misconception: "scope_error — gradient descent can get stuck in local minima"
4. SymPy confirms: compute ∂L/∂w symbolically to show multiple minima exist
5. Socratic engine generates: "Interesting — can you draw a loss curve that would make that impossible?"
6. Knowledge tracker embeds this exchange, updates user's gradient_descent_mechanics score
7. Response + KaTeX-rendered math sent back to React
8. React displays: Socratic question + misconception badge + updated knowledge map
```

---

## Phase 0 — Environment Setup
**Timeline:** Weeks 1–2  
**Goal:** A working development environment and your first Git repository

### What you learn
- Terminal / command line navigation
- Git and GitHub (version control)
- VS Code setup and extensions
- Python virtual environments
- Node.js for React later

### Installation on Pop!_OS

```bash
# Check what you already have
python3 --version    # want 3.10, 3.11, or 3.12
pip3 --version
git --version

# Install anything missing
sudo apt install python3-pip git -y

# Install Node.js (for React in Phase 6)
# Go to nodejs.org — download LTS version
node --version    # verify: should say v20.x
```

### Project folder creation

```bash
cd ~/Documents
mkdir socratic-ml-tutor
cd socratic-ml-tutor
mkdir backend frontend
cd backend
```

### Virtual environment — the most important habit

A virtual environment is an isolated Python installation just for this project. Every Python project gets its own. This prevents packages from different projects conflicting.

```bash
# Create (once per project)
python3 -m venv venv

# Activate (every time you open a terminal for this project)
source venv/bin/activate

# You know it's active when you see (venv) at the start of your prompt:
# (venv) vishruth@pop-os:~/Documents/socratic-ml-tutor/backend$

# Deactivate when done
deactivate
```

### VS Code extensions to install
- Python (by Microsoft) — syntax highlighting, intellisense
- Prettier — auto-formats code
- GitLens — shows Git history inline
- Thunder Client — test your API without leaving VS Code

### Git setup (do this once ever, not per project)

```bash
git config --global user.name "Vishruth"
git config --global user.email "your@email.com"

# Initialize your project repo
cd ~/Documents/socratic-ml-tutor
git init
git remote add origin https://github.com/YOUR_USERNAME/socratic-ml-tutor.git
```

### The three Git commands you will use forever

```bash
git add .                           # stage all changes
git commit -m "what you changed"    # save a snapshot
git push                            # upload to GitHub
```

### .gitignore — create this immediately

```bash
cat > backend/.gitignore << 'EOF'
venv/
.env
__pycache__/
*.pyc
.DS_Store
firebase-service-account.json
chroma_data/
EOF
```

### Milestone
You can run `python3 main.py` and push code to GitHub. Your project repo is live.

---

## Phase 1 — Python Core
**Timeline:** Weeks 2–4  
**Goal:** Understand Python well enough to build real software, not just scripts

### What you learn
Variables and types, control flow, functions, classes (OOP), modules, file I/O, type hints

### Key concept 1 — Data types

```python
# Types you will use constantly in this project
name = "Vishruth"       # str
age = 20                # int
confidence = 0.87       # float
is_correct = True       # bool

# dict — the most important. Your API returns these. Your DB gives you these.
problem = {
    "input": "integrate x^2",
    "topic": "calculus",
    "difficulty": "basic",
    "user_id": "abc-123"
}
# Access:
print(problem["topic"])        # calculus
print(problem.get("hint"))     # None — safe, no crash if key missing

# list — ordered collection
steps = ["identify function", "apply power rule", "add constant C"]
steps.append("verify by differentiating")
print(steps[0])    # first: "identify function"
print(steps[-1])   # last: "verify by differentiating"
```

### Key concept 2 — Functions

```python
def classify_problem(problem_text: str) -> str:
    """
    The -> str is a type hint. It tells anyone reading this code
    what type this function returns. Use these always.
    """
    text = problem_text.lower()

    if "integrate" in text or "∫" in text:
        return "calculus"
    elif "matrix" in text or "eigenvalue" in text:
        return "linear_algebra"
    elif "gradient" in text or "backprop" in text:
        return "ml_math"
    else:
        return "general_algebra"

topic = classify_problem("Find the eigenvalues of this matrix")
print(topic)  # linear_algebra
```

### Key concept 3 — Classes (OOP)

Every major component of this project is a class. A class is a blueprint: it defines what data something has (attributes) and what it can do (methods).

```python
class SocraticSession:
    """One tutoring conversation between a user and the AI."""

    def __init__(self, user_id: str, topic: str):
        # __init__ runs when you create a new SocraticSession()
        self.user_id = user_id
        self.topic = topic
        self.messages = []            # conversation history
        self.concepts_tested = []     # what has been covered
        self.understanding_score = 0  # 0 to 100

    def add_message(self, role: str, content: str):
        """role is 'user' or 'model' (Gemini uses 'model' not 'assistant')"""
        self.messages.append({"role": role, "content": content})

    def get_history(self) -> list:
        """Return last 10 messages for context window management"""
        return self.messages[-10:]

    def update_score(self, correct: bool):
        if correct:
            self.understanding_score = min(100, self.understanding_score + 10)
        else:
            self.understanding_score = max(0, self.understanding_score - 5)

# Usage:
session = SocraticSession(user_id="vishruth-01", topic="gradient_descent")
session.add_message("user", "I think gradient descent always finds the global minimum")
session.add_message("model", "Interesting — can you think of a loss curve where that would be impossible?")
print(session.understanding_score)   # 0 (they showed a misconception)
```

### What you build
A Python CLI math quiz — you type a question in terminal, the program evaluates your answer.

### Milestone
You write a Python class from scratch without looking at examples.

---

## Phase 2 — FastAPI Backend
**Timeline:** Weeks 4–6  
**Goal:** A running web server with real API endpoints you can test

### What you learn
How HTTP works, REST API design, FastAPI syntax, Pydantic models, async/await, CORS

### The mental model for web servers

```
Browser (or React app) visits: http://localhost:8000/api/ask
                    ↓
FastAPI receives the request (a POST with JSON body)
                    ↓
Finds the function decorated with @app.post("/api/ask")
                    ↓
Runs your Python function, gets a result
                    ↓
Converts result to JSON, sends it back
                    ↓
Browser/React receives: {"reply": "What makes you think that?"}
```

### Installation

```bash
# In backend/ with venv active
pip install fastapi uvicorn[standard] python-dotenv httpie
pip freeze > requirements.txt
```

### First working server

```python
# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Socratic ML Tutor API", version="0.1")

# CORS: allows your React frontend (port 3000) to call this backend (port 8000)
# Without this, the browser blocks cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model: defines exactly what shape of data this endpoint accepts
# FastAPI automatically validates incoming requests against this
# Wrong data type = automatic 422 error, no code needed from you
class AskRequest(BaseModel):
    question: str           # required
    topic: str = "general"  # optional with default
    history: list = []      # conversation history

class AskResponse(BaseModel):
    reply: str
    should_reveal: bool
    concepts_touched: list[str]

@app.get("/")
def root():
    return {"status": "alive", "project": "Socratic ML Tutor"}

@app.get("/health")
def health():
    return {"healthy": True}

@app.post("/api/ask", response_model=AskResponse)
async def ask_tutor(request: AskRequest):
    # async means this won't block the server while waiting for Gemini
    # FastAPI handles other requests while this one waits for the AI
    return AskResponse(
        reply=f"You asked: {request.question} — What makes you think that?",
        should_reveal=False,
        concepts_touched=[request.topic]
    )
```

### Running the server

```bash
uvicorn main:app --reload
# main = the filename (main.py)
# app = the variable (app = FastAPI(...))
# --reload = restart automatically when you save changes
```

Visit these URLs immediately:
- `http://localhost:8000` → your root endpoint response
- `http://localhost:8000/docs` → **interactive API docs (Swagger UI)** — test endpoints in browser
- `http://localhost:8000/redoc` → alternative documentation

### HTTP status codes to memorize

| Code | Meaning | When it happens |
|------|---------|----------------|
| 200 | OK | Request succeeded |
| 201 | Created | You saved something new to the DB |
| 400 | Bad Request | Client sent wrong data |
| 401 | Unauthorized | Not logged in |
| 403 | Forbidden | Logged in but no permission |
| 404 | Not Found | Resource doesn't exist |
| 422 | Validation Error | Pydantic rejected the request shape |
| 500 | Server Error | Your code crashed |

### Using the freeCodeCamp video
Watch everything. Skip: database integration (Phase 5), background tasks (Phase 8).  
Actively code along: path parameters, query parameters, request body, Pydantic, async/await.

When the video uses OpenAI:
```python
# Video does this (OpenAI):
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(model="gpt-4", messages=[...])
text = response.choices[0].message.content

# You do this (Gemini):
import google.generativeai as genai
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("your prompt")
text = response.text
```

### Milestone
You can open Thunder Client (VS Code) or your browser's `/docs` page, send a POST to `/api/ask`, and get a JSON response back.

---

## Phase 3 — Math Engine with SymPy
**Timeline:** Weeks 6–8  
**Goal:** Exact symbolic math computation — the engine that makes your AI always mathematically correct

### What you learn
Symbolic vs numeric computation, SymPy library, LaTeX syntax, math problem taxonomy

### The key insight
A regular calculator: `√2 = 1.41421356...` (approximation, can accumulate errors)  
SymPy: `√2 = √2` (exact symbolic truth, always perfect)

This matters because your Socratic tutor must never give a wrong answer. SymPy guarantees correctness.

### Installation

```bash
pip install sympy
```

### Core SymPy concepts

```python
import sympy as sp

# Define symbolic variables (not numbers — symbols)
x = sp.Symbol('x')
theta = sp.Symbol('theta')   # used constantly in ML math
alpha = sp.Symbol('alpha')   # learning rate

# Basic operations
expr = x**3 + 2*x
print(sp.latex(expr))          # x^{3} + 2 x  (LaTeX string for rendering)

# Differentiation — critical for teaching backprop
derivative = sp.diff(x**3 + 2*x, x)
print(derivative)              # 3*x**2 + 2
print(sp.latex(derivative))    # 3 x^{2} + 2

# Integration
integral = sp.integrate(x**2, x)
print(integral)                # x**3/3
print(sp.latex(integral))      # \frac{x^{3}}{3}

# Definite integral
definite = sp.integrate(sp.exp(-x**2), (x, 0, sp.oo))
print(definite)                # sqrt(pi)/2  ← EXACT, not approximate

# Solving equations
solution = sp.solve(x**2 - 4, x)
print(solution)                # [-2, 2]

# Matrix operations (linear algebra for ML)
A = sp.Matrix([[1, 2], [3, 4]])
print(A.det())                 # -2
print(A.eigenvals())           # {-0.372...: 1, 5.372...: 1}
print(sp.latex(A.inv()))       # LaTeX of the inverse matrix

# Verifying student answers (mathematically equivalent, not string equal)
student_answer = sp.sympify("x**3/3 + x")
correct_answer = sp.sympify("x + x**3/3")
difference = sp.simplify(student_answer - correct_answer)
print(difference == 0)         # True — they ARE the same expression
```

### The MathEngine class (the full implementation)

```python
# backend/services/math_engine.py
import sympy as sp

class MathEngine:
    """
    Computes exact mathematical answers and step-by-step solutions.
    Used by the Socratic tutor to:
    1. Know the correct answer (so it can guide without revealing)
    2. Verify student answers mathematically
    3. Generate structured steps for hints
    """

    def __init__(self):
        self.x = sp.Symbol('x')
        self.y = sp.Symbol('y')
        self.theta = sp.Symbol('theta')
        self.alpha = sp.Symbol('alpha')   # learning rate in ML

    def differentiate(self, expr_str: str, variable: str = 'x') -> dict:
        var = sp.Symbol(variable)
        expr = sp.sympify(expr_str)
        derivative = sp.diff(expr, var)

        return {
            "answer_latex": sp.latex(derivative),
            "answer_str": str(derivative),
            "steps": [
                f"Starting expression: ${sp.latex(expr)}$",
                f"Apply differentiation with respect to ${variable}$",
                f"Result: ${sp.latex(derivative)}$"
            ],
            "is_zero": derivative == 0
        }

    def integrate(self, expr_str: str, variable: str = 'x') -> dict:
        var = sp.Symbol(variable)
        expr = sp.sympify(expr_str)
        integral = sp.integrate(expr, var)

        return {
            "answer_latex": sp.latex(integral) + " + C",
            "answer_str": str(integral),
            "steps": [
                f"Integrate: $\\int {sp.latex(expr)}\\, d{variable}$",
                f"Apply integration rules",
                f"Result: ${sp.latex(integral)} + C$"
            ]
        }

    def compute_gradient(self, loss_expr_str: str, params: list[str]) -> dict:
        """
        Compute partial derivatives of a loss function.
        This is literally what backpropagation computes.
        """
        loss = sp.sympify(loss_expr_str)
        gradients = {}

        for param_name in params:
            param = sp.Symbol(param_name)
            grad = sp.diff(loss, param)
            gradients[param_name] = {
                "latex": sp.latex(grad),
                "str": str(grad),
                "hint": "The gradient points uphill — gradient descent moves opposite to this"
            }

        return {
            "loss_latex": sp.latex(loss),
            "gradients": gradients
        }

    def verify_student_answer(self, student: str, correct: str,
                               variable: str = 'x') -> dict:
        """
        Check if student's answer is mathematically equivalent to correct one.
        x+1 and 1+x are the same. SymPy knows this.
        """
        try:
            student_expr = sp.sympify(student)
            correct_expr = sp.sympify(correct)
            is_correct = sp.simplify(student_expr - correct_expr) == 0

            return {
                "is_correct": is_correct,
                "feedback": "Correct!" if is_correct
                    else f"Not quite. You have ${sp.latex(student_expr)}$, we need ${sp.latex(correct_expr)}$"
            }
        except Exception as e:
            return {"is_correct": False, "feedback": f"Couldn't parse your answer: {e}"}
```

### Book reference for this phase
**Chapter 4 of Hands-On ML (pp. 106–140)** — "Training Models"  
Read the full derivation of gradient descent. This is the math your tutor will teach. Understanding it deeply makes you a better prompt engineer for the Socratic engine.

### Milestone
`MathEngine().differentiate("x**3 + 2*x")` returns a dict with `answer_latex: "3 x^{2} + 2"` and a list of steps.

---

## Phase 4 — The Socratic AI Brain
**Timeline:** Weeks 8–12  
**Goal:** An AI that teaches by asking questions, never by answering directly

### What you learn
How LLMs work conceptually, Google AI Studio / Gemini API, prompt engineering, the Socratic method, misconception detection, conversation history management

### The system prompt — the most important code in the project

```python
# backend/services/socratic_engine.py
SOCRATIC_SYSTEM_PROMPT = """
You are a Socratic mathematics tutor specializing in the mathematical
foundations of machine learning. Your core rule, which you NEVER break:

NEVER give the answer directly. Always respond with a guiding question.

Your conversation goals in order:
1. First, probe what the student already understands
2. Identify the specific gap or misconception in their thinking
3. Ask one targeted question that nudges them one step closer
4. Only after the student has reasoned through all steps, confirm and deepen

When you detect a misconception, name it explicitly before asking:
"I notice you might be thinking of X as Y — let's examine that assumption..."

Topics you teach (the math BEHIND ML, not just ML):
- Gradient descent: partial derivatives, chain rule, cost surfaces
- Backpropagation: chain rule through computational graphs
- Linear algebra for ML: matrix multiplication, eigendecomposition, SVD
- Probability & statistics: Bayes theorem, distributions, MLE
- Calculus for optimization: gradients, Hessians, saddle points
- Information theory: entropy, cross-entropy loss, KL divergence

Response format rules:
- Keep responses SHORT — one question at a time, never lecture
- If the student is clearly stuck after 3 exchanges, give a small hint
- Use LaTeX for math: $\\frac{\\partial L}{\\partial w}$
- End EVERY response with exactly one question
- Gauge difficulty from student's language and adjust accordingly

You know the correct answer (provided in [CORRECT_ANSWER]) but reveal it
only when the student has demonstrated they understand the underlying
concepts, not just the final number.
"""
```

### Gemini API integration

```bash
# Install
pip install google-generativeai
```

```python
# backend/services/socratic_engine.py  (full implementation)
import google.generativeai as genai
from dotenv import load_dotenv
import os, json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class SocraticEngine:

    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            system_instruction=SOCRATIC_SYSTEM_PROMPT
        )

    def respond(self, user_message: str, history: list[dict],
                correct_answer: str, topic: str) -> dict:
        """
        history format for Gemini:
        [{"role": "user", "parts": ["message"]},
         {"role": "model", "parts": ["reply"]}]

        Note: Gemini uses "model" (not "assistant") and "parts" (not "content")
        """
        chat = self.model.start_chat(history=history)

        # Tell the AI the correct answer without letting it reveal it
        augmented = f"""
        [TUTOR CONTEXT — DO NOT REVEAL: correct answer = {correct_answer}]
        [Topic: {topic}]
        [Student says]: {user_message}
        """

        response = chat.send_message(augmented)
        reply = response.text

        # Build updated history for storage
        updated_history = history + [
            {"role": "user", "parts": [user_message]},
            {"role": "model", "parts": [reply]}
        ]

        return {
            "reply": reply,
            "updated_history": updated_history,
            "should_reveal": len(history) >= 10  # 5 full exchanges
        }

    def detect_misconception(self, student_text: str, topic: str) -> dict:
        """Classify what the student's response reveals about their understanding"""
        prompt = f"""
        A student learning {topic} said: "{student_text}"

        Classify their understanding. Return ONLY valid JSON, nothing else:
        {{
            "has_misconception": true or false,
            "type": "conceptual_confusion | sign_error | scope_error | correct | partial",
            "what_they_think": "their apparent mental model in one sentence",
            "target_concept": "the specific concept they need to grasp"
        }}
        """

        classifier = genai.GenerativeModel("gemini-2.0-flash")
        response = classifier.generate_content(prompt)

        try:
            text = response.text.strip().removeprefix("```json").removesuffix("```").strip()
            return json.loads(text)
        except json.JSONDecodeError:
            return {"has_misconception": False, "type": "unknown"}
```

### How the Socratic interaction should look

```
User: "I think gradient descent always finds the global minimum"

BAD response (what every other tool does):
"Gradient descent does not always find the global minimum.
 It can get stuck in local minima..."

GOOD response (what your tutor does):
"Interesting. Before we examine that — can you sketch in your
 mind what a loss surface with multiple valleys would look like?
 What would gradient descent do if it started in the wrong valley?"
```

### Book references for this phase
- **Chapter 1 (pp. 1–40):** The ML Landscape — read so you understand what the LLM is doing conceptually
- **Chapter 16 (pp. 537–580):** NLP with Attention — how transformers (the thing Gemini IS) work internally. Makes you a better prompt engineer.

### Misconception taxonomy (build this into your system)

| Type | Example | What it means |
|------|---------|---------------|
| `conceptual_confusion` | "derivative and gradient are the same thing" | Confusing related but distinct concepts |
| `sign_error` | "gradient descent adds the gradient" | Right concept, wrong direction |
| `scope_error` | "gradient descent always finds global minimum" | Right mechanism, wrong generalization |
| `partial` | Gets the formula right but can't explain it | Procedural knowledge without conceptual understanding |
| `correct` | Can explain why AND derive the formula | Genuine understanding |

### Milestone
Ask your tutor "What is backpropagation?" — it replies with a question, not a definition.

---

## Phase 5 — Database and Authentication
**Timeline:** Weeks 12–14  
**Goal:** Users can sign up, log in, and have their sessions saved permanently

### What you learn
SQL basics, PostgreSQL, SQLAlchemy ORM, Alembic migrations, Firebase Auth, Redis caching, environment variables

### The mental model for databases
A database is a collection of spreadsheets (tables) that can reference each other. PostgreSQL is the software that manages these tables. SQLAlchemy is the Python layer that lets you talk to PostgreSQL using Python classes instead of raw SQL.

### SQL you must write by hand first (build the intuition)

```sql
-- Run these in psql terminal before using SQLAlchemy
-- This is what SQLAlchemy generates under the hood

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    firebase_uid VARCHAR(255) UNIQUE NOT NULL,  -- from Firebase Auth
    email VARCHAR(255) UNIQUE NOT NULL,
    display_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    topic VARCHAR(100),
    understanding_score INTEGER DEFAULT 0,
    started_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(id) ON DELETE CASCADE,
    role VARCHAR(20),           -- 'user' or 'model'
    content TEXT,
    misconception_detected JSONB,  -- stores the classification result
    created_at TIMESTAMP DEFAULT NOW()
);
```

### SQLAlchemy models (Python classes ↔ database tables)

```python
# backend/models/user.py
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    firebase_uid = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    display_name = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

    sessions = relationship("Session", back_populates="user")

class Session(Base):
    __tablename__ = "sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    topic = Column(String(100))
    understanding_score = Column(Integer, default=0)
    started_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="sessions")
    messages = relationship("Message", back_populates="session",
                           order_by="Message.created_at")

class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.id"), nullable=False)
    role = Column(String(20))           # 'user' or 'model'
    content = Column(Text)
    misconception_detected = Column(JSONB, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("Session", back_populates="messages")
```

### Firebase Authentication (replaces custom JWT)

Firebase Auth saves you from building login from scratch. Building JWT auth correctly (password hashing, refresh tokens, token rotation, session invalidation) takes weeks and is easy to get wrong. Firebase gives it to you in 5 lines.

```bash
# Backend
pip install firebase-admin

# Download your service account key:
# Firebase Console → Project Settings → Service Accounts → Generate new private key
# Save as: backend/firebase-service-account.json
# ADD THIS TO .gitignore IMMEDIATELY
```

```python
# backend/auth.py
import firebase_admin
from firebase_admin import credentials, auth
from fastapi import HTTPException, Header

cred = credentials.Certificate("firebase-service-account.json")
firebase_admin.initialize_app(cred)

def verify_firebase_token(authorization: str = Header(...)) -> dict:
    """
    FastAPI dependency. Add Depends(verify_firebase_token) to any
    endpoint that requires the user to be logged in.
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")

    token = authorization.split(" ")[1]

    try:
        return auth.verify_id_token(token)  # returns dict with uid, email, name
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# Usage in an endpoint:
# @app.post("/api/ask")
# async def ask(request: AskRequest, user=Depends(verify_firebase_token)):
#     user_id = user["uid"]   # the verified Firebase user ID
```

### Redis — session memory

Redis keeps the last N messages of each conversation in memory so the AI has context without hitting the database on every request.

```python
# backend/services/session_cache.py
import redis, json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def store_conversation(user_id: str, session_id: str, messages: list):
    """Store last 20 messages — sliding window"""
    key = f"conv:{user_id}:{session_id}"
    r.set(key, json.dumps(messages[-20:]), ex=3600)  # expires in 1 hour

def get_conversation(user_id: str, session_id: str) -> list:
    key = f"conv:{user_id}:{session_id}"
    data = r.get(key)
    return json.loads(data) if data else []
```

### Milestone
Sign up, log in, ask a question, log out, log back in — your session history is still there.

---

## Phase 6 — React Frontend
**Timeline:** Weeks 14–18  
**Goal:** A beautiful, working user interface that renders math beautifully

### What you learn
HTML & CSS foundations, JavaScript essentials (async/await, .map()), React components, useState, useEffect, props, API calls, KaTeX math rendering, React Router

### The React mental model
```
State = { messages: [], isLoading: false, input: "" }
              ↓
UI = f(state)   ← React renders whatever the current state says
              ↓
User types → setInput("new value") → React re-renders automatically
```

You never manually update the DOM. You update state. React handles the rest.

### Installation

```bash
cd ~/Documents/socratic-ml-tutor/frontend
npx create-react-app socratic-ui
cd socratic-ui
npm install katex react-katex axios firebase react-router-dom
```

### The main chat component

```jsx
// frontend/src/components/SocraticChat.jsx
import { useState, useRef, useEffect } from "react";
import { BlockMath, InlineMath } from "react-katex";
import "katex/dist/katex.min.css";
import { auth } from "../firebase";

export function SocraticChat({ topic, sessionId }) {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const bottomRef = useRef(null);

    // Auto-scroll to bottom on new messages
    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMsg = { role: "user", content: input };
        setMessages(prev => [...prev, userMsg]);  // show immediately
        setInput("");
        setIsLoading(true);

        try {
            const token = await auth.currentUser.getIdToken();

            const res = await fetch("http://localhost:8000/api/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({ question: input, topic, session_id: sessionId })
            });

            const data = await res.json();
            setMessages(prev => [...prev, { role: "model", content: data.reply }]);

        } catch (err) {
            console.error(err);
        } finally {
            setIsLoading(false);
        }
    };

    // Render LaTeX inline: $\frac{x}{2}$ inside normal text
    const renderContent = (text) => {
        const parts = text.split(/(\$[^$]+\$)/g);
        return parts.map((part, i) => {
            if (part.startsWith("$") && part.endsWith("$")) {
                return <InlineMath key={i} math={part.slice(1, -1)} />;
            }
            return <span key={i}>{part}</span>;
        });
    };

    return (
        <div className="chat-container">
            <div className="messages">
                {messages.map((msg, i) => (
                    <div key={i} className={`message ${msg.role}`}>
                        {renderContent(msg.content)}
                    </div>
                ))}
                {isLoading && <div className="message model loading">Thinking...</div>}
                <div ref={bottomRef} />
            </div>

            <div className="input-area">
                <textarea
                    value={input}
                    onChange={e => setInput(e.target.value)}
                    onKeyDown={e => e.key === "Enter" && !e.shiftKey && sendMessage()}
                    placeholder="Explain your thinking... or ask a question"
                    rows={3}
                />
                <button onClick={sendMessage} disabled={isLoading}>
                    {isLoading ? "..." : "Send"}
                </button>
            </div>
        </div>
    );
}
```

### Firebase frontend setup

```javascript
// frontend/src/firebase.js
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup,
         signInWithEmailAndPassword, createUserWithEmailAndPassword,
         signOut, onAuthStateChanged } from "firebase/auth";

const firebaseConfig = {
    // paste your config from Firebase Console here
    apiKey: "AIza...",
    authDomain: "socratic-ml-tutor.firebaseapp.com",
    projectId: "socratic-ml-tutor",
    // ...
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const googleProvider = new GoogleAuthProvider();

export const loginWithGoogle = () => signInWithPopup(auth, googleProvider);
export const loginWithEmail = (e, p) => signInWithEmailAndPassword(auth, e, p);
export const register = (e, p) => createUserWithEmailAndPassword(auth, e, p);
export const logout = () => signOut(auth);
export const onAuthChange = (cb) => onAuthStateChanged(auth, cb);
```

### Milestone
You open `localhost:3000`, type a question, and get a Socratic reply rendered in beautiful LaTeX notation.

---

## Phase 7 — Knowledge Tracking with Embeddings
**Timeline:** Weeks 18–20  
**Goal:** A visual map of exactly what the student understands about ML mathematics

### What you learn
What embeddings are, Gemini Embeddings API, ChromaDB vector database, cosine similarity, knowledge graph concept, spaced repetition logic

### What embeddings are (the key concept)

An embedding converts text into a list of numbers (a vector) such that similar meanings produce similar number patterns.

```
"gradient descent mechanics"  →  [0.21, -0.43, 0.87, 0.12, ...]  (768 numbers)
"learning rate in training"   →  [0.22, -0.41, 0.85, 0.14, ...]  (very similar!)
"matrix determinant"          →  [-0.31, 0.66, -0.12, 0.55, ...]  (very different)
```

ChromaDB stores these vectors and can find the most similar ones by measuring the angle between them (cosine similarity). This is how your knowledge tracker finds which concepts a student has engaged with.

### Gemini Embeddings (replaces OpenAI embeddings, free)

```python
import google.generativeai as genai

result = genai.embed_content(
    model="models/text-embedding-004",
    content="gradient descent mechanics",
    task_type="retrieval_document"
)
vector = result["embedding"]  # list of 768 floats
```

### The Knowledge Tracker

```python
# backend/services/knowledge_tracker.py
import chromadb
import google.generativeai as genai

class KnowledgeTracker:

    ML_MATH_CONCEPTS = [
        "gradient_descent_mechanics",
        "partial_derivatives",
        "chain_rule_backprop",
        "matrix_multiplication",
        "eigenvalues_eigenvectors",
        "cross_entropy_loss",
        "bayesian_probability",
        "attention_mechanism_math",
        "softmax_function",
        "batch_normalization_math",
    ]

    def __init__(self):
        self.chroma = chromadb.PersistentClient(path="./chroma_data")
        self.collection = self.chroma.get_or_create_collection("student_knowledge")

    def embed(self, text: str) -> list[float]:
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_document"
        )
        return result["embedding"]

    def record_exchange(self, user_id: str, student_message: str,
                        misconception_data: dict, topic: str):
        """After each exchange, store what the student demonstrated"""
        embedding = self.embed(student_message)
        understanding_level = self._score(misconception_data)

        self.collection.add(
            ids=[f"{user_id}_{topic}_{hash(student_message)}"],
            embeddings=[embedding],
            documents=[student_message],
            metadatas=[{
                "user_id": user_id,
                "topic": topic,
                "understanding_level": understanding_level,
                "misconception_type": misconception_data.get("type", "unknown")
            }]
        )

    def get_knowledge_map(self, user_id: str) -> dict:
        """Return understanding scores for all ML math concepts"""
        knowledge_map = {}

        for concept in self.ML_MATH_CONCEPTS:
            concept_embedding = self.embed(concept.replace("_", " "))

            results = self.collection.query(
                query_embeddings=[concept_embedding],
                n_results=10,
                where={"user_id": user_id}
            )

            if results["metadatas"][0]:
                scores = [m["understanding_level"] for m in results["metadatas"][0]]
                avg = sum(scores) / len(scores)
                misconceptions = [m["misconception_type"] for m in results["metadatas"][0]
                                  if m["misconception_type"] not in ["correct", "unknown"]]

                knowledge_map[concept] = {
                    "score": round(avg, 1),
                    "status": "understood" if avg >= 80 else "developing" if avg >= 50 else "misconception",
                    "misconceptions_seen": list(set(misconceptions)),
                    "exchanges": len(scores)
                }
            else:
                knowledge_map[concept] = {"score": 0, "status": "not_started",
                                           "misconceptions_seen": [], "exchanges": 0}

        return knowledge_map

    def _score(self, misconception_data: dict) -> float:
        return {"correct": 90, "partial": 60, "conceptual_confusion": 25,
                "sign_error": 50, "scope_error": 35, "unknown": 40}.get(
                    misconception_data.get("type", "unknown"), 40)
```

### Book reference for this phase
**Chapter 16 (pp. 537–560):** Word embeddings and attention — the conceptual foundation for exactly what ChromaDB does.

### Milestone
After 5 questions about gradient descent, the UI shows a knowledge map with colour-coded concept nodes showing what the student understands vs. misunderstands.

---

## Phase 8 — Vision Pipeline and Deployment
**Timeline:** Weeks 20–22  
**Goal:** Users can upload photos of math problems + the app is live on the internet

### What you learn
How OCR works, Pix2Tex, GPT-4o Vision fallback, file upload in FastAPI, Docker basics, Docker Compose, Cloud Run, Firebase Hosting

### The image-to-LaTeX pipeline

Two stages: Pix2Tex for clean printed formulas, GPT-4o Vision as fallback for handwriting and messy photos.

```bash
pip install pix2tex google-cloud-storage
```

```python
# backend/services/vision_service.py
import pix2tex
from PIL import Image
import io, base64
import google.generativeai as genai

class VisionService:
    def __init__(self):
        self.ocr_model = pix2tex.LatexOCR()

    def image_to_latex(self, image_bytes: bytes) -> dict:
        image = Image.open(io.BytesIO(image_bytes))

        # Stage 1: Pix2Tex (fast, free, great for printed formulas)
        try:
            latex = self.ocr_model(image)
            if any(c in latex for c in ['\\', '^', '_', 'frac', 'int']):
                return {"latex": latex, "method": "pix2tex", "confidence": "high"}
        except Exception:
            pass

        # Stage 2: Gemini Vision (handles handwriting, context)
        b64 = base64.b64encode(image_bytes).decode()
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content([
            {"mime_type": "image/jpeg", "data": b64},
            "Extract all mathematical expressions. Return ONLY LaTeX code."
        ])
        return {"latex": response.text, "method": "gemini_vision", "confidence": "high"}
```

### Why CNN from your book applies here (conceptual, not implementation)
You will NOT train a CNN from scratch. Pix2Tex IS a CNN-based model — trained by researchers on millions of math images. Your book's Chapter 14 (CNNs) teaches you how it works internally. That understanding helps you know when Pix2Tex will fail (very stylized fonts, vertical fractions, tables) and when to route to the Gemini Vision fallback.

### Docker — packaging your entire app

```dockerfile
# backend/Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

```yaml
# docker-compose.yml (root folder) — start everything with: docker compose up
services:
  backend:
    build: ./backend
    ports: ["8000:8080"]
    env_file: backend/.env
    depends_on: [db, redis]

  frontend:
    build: ./frontend
    ports: ["3000:80"]

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: socratic_tutor
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes: ["pgdata:/var/lib/postgresql/data"]

  redis:
    image: redis:7-alpine

volumes:
  pgdata:
```

### Deploy to Google Cloud Run (Phase 8 end)

```bash
# Install gcloud CLI from cloud.google.com/sdk/docs/install
gcloud auth login
gcloud config set project socratic-ml-tutor

# Deploy backend
gcloud run deploy socratic-tutor-backend \
  --source ./backend \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated

# Deploy frontend to Firebase Hosting
npm install -g firebase-tools
cd frontend
npm run build
firebase deploy
```

### Book references for this phase
- **Chapter 14 (pp. 452–500):** CNNs — understand how Pix2Tex works internally
- **Chapter 19 (pp. 655–690):** Deploying Models — deployment principles for your stack

### Milestone
You share a URL. Someone opens it on their phone, uploads a photo of a textbook formula, gets a Socratic tutoring session. The app is live.

---

## 14. Book Chapter Map

This is the exact reading list from *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow* (Aurélien Géron). These are the only chapters directly relevant to this project.

| Chapter | Pages | Topic | When to read | Why it matters for this project |
|---------|-------|-------|-------------|--------------------------------|
| Chapter 1 | pp. 1–40 | The ML Landscape | Before Phase 0 | Vocabulary you need for everything. Trains, inference, parameters, loss — all defined here |
| Chapter 4 | pp. 106–140 | Training Models (gradient descent) | Phase 3 | Derives the math your tutor teaches. Read it before building the math engine |
| Chapter 14 | pp. 452–500 | CNNs | Phase 8 | Conceptual basis for Pix2Tex. Explains feature detection, convolution, pooling |
| Chapter 16 | pp. 537–560 | Word embeddings, Word2Vec | Phase 7 | Foundation for ChromaDB and the knowledge tracker |
| Chapter 16 | pp. 560–580 | Attention mechanisms, Transformers | Phase 4 | How Gemini works. Makes you a better prompt engineer |
| Chapter 19 | pp. 655–690 | Deploying ML models | Phase 8 | Docker, cloud deployment principles |

### Chapters you can skip for this project
Chapters 2–3 (classical ML algorithms), 5–9 (SVMs, decision trees, random forests, ensemble methods), 10–13 (deep learning from scratch, training tricks, custom layers), 15 (RNNs), 17 (autoencoders), 18 (reinforcement learning).

These are genuinely valuable chapters — just not needed for what you are building. Save them for future projects.

---

## 15. Google Services Setup Guide

### Google AI Studio (Gemini — your LLM)
1. Go to `aistudio.google.com`
2. Sign in with your Google account
3. Click "Get API Key" → "Create API key in new project"
4. Copy the key (starts with `AIza`)
5. Add to `backend/.env`: `GEMINI_API_KEY=AIza...`

```bash
pip install google-generativeai python-dotenv

# Quick test:
python3 -c "
import google.generativeai as genai, os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')
print(model.generate_content('Say: Socratic tutor ready.').text)
"
```

### Firebase (Authentication + Frontend Hosting)
1. Go to `console.firebase.google.com`
2. "Add project" → name: `socratic-ml-tutor`
3. Disable Google Analytics for now → Create project
4. Left sidebar → Authentication → "Get started"
5. Enable "Email/Password" and "Google" sign-in methods
6. Project settings → "Your apps" → `</>` (web) → Register → copy `firebaseConfig`
7. Project settings → Service Accounts → Generate new private key → save as `backend/firebase-service-account.json`
8. **Immediately add `firebase-service-account.json` to `.gitignore`**

### Google Cloud Storage (file uploads)
1. Go to `console.cloud.google.com`
2. Left menu → Cloud Storage → Create bucket
3. Name: `socratic-ml-tutor-uploads`
4. Region: `asia-south1` (closest to Bengaluru)
5. Create

```bash
pip install google-cloud-storage
# Authentication uses Application Default Credentials
gcloud auth application-default login
```

### Google Colab (learning sandbox)
- Go to `colab.research.google.com`
- New notebook → prototype every Phase's concepts before writing production code
- Notebooks auto-save to Google Drive at `My Drive/Colab Notebooks/`

**Recommended notebooks to create:**
- `sympy_experiments.ipynb` — test all SymPy functions (Phase 3)
- `gemini_prompt_testing.ipynb` — iterate system prompts fast (Phase 4)
- `embeddings_exploration.ipynb` — visualize what embeddings look like (Phase 7)

---

## 16. Daily Workflow

### Every day you sit down to work

```bash
# 1. Navigate to project
cd ~/Documents/socratic-ml-tutor/backend

# 2. Activate virtual environment (always do this first)
source venv/bin/activate
# Prompt changes to: (venv) vishruth@...

# 3. Start the backend server
uvicorn main:app --reload

# 4. Open VS Code (new terminal or window)
code .

# 5. Open frontend (separate terminal)
cd ../frontend/socratic-ui
npm start
```

### Rhythm at 2 hours/day
- **30 minutes:** Study the current phase's concepts (book chapter + official docs)
- **60 minutes:** Write code for the current phase's build target
- **30 minutes:** Test what you built, break it on purpose, fix it, commit to GitHub

### End of every session
```bash
git add .
git commit -m "phase X: describe what you built today"
git push
deactivate   # exit the venv
```

### End of every phase
- The milestone statement for that phase must be demonstrably true
- Do not move to the next phase until it is
- The milestone is your test

---

## 17. Complete Folder Structure

```
socratic-ml-tutor/
├── backend/
│   ├── venv/                        ← never touch manually
│   ├── main.py                      ← FastAPI application entry point
│   ├── auth.py                      ← Firebase token verification
│   ├── database.py                  ← SQLAlchemy engine + session
│   ├── .env                         ← secrets (NEVER commit to Git)
│   ├── .gitignore
│   ├── requirements.txt
│   ├── firebase-service-account.json  ← secret (in .gitignore)
│   ├── Dockerfile
│   ├── models/
│   │   ├── user.py                  ← User SQLAlchemy model
│   │   ├── session.py               ← Session model
│   │   └── message.py               ← Message model
│   ├── routers/
│   │   ├── ask.py                   ← /api/ask endpoint
│   │   ├── sessions.py              ← session CRUD endpoints
│   │   ├── knowledge.py             ← /api/knowledge-map endpoint
│   │   └── upload.py                ← /api/upload-math-image endpoint
│   └── services/
│       ├── math_engine.py           ← SymPy symbolic computation
│       ├── socratic_engine.py       ← Gemini Socratic AI
│       ├── knowledge_tracker.py     ← ChromaDB embeddings
│       ├── vision_service.py        ← Pix2Tex + Gemini Vision OCR
│       └── storage_service.py       ← Google Cloud Storage
│
├── frontend/
│   └── socratic-ui/
│       ├── public/
│       └── src/
│           ├── firebase.js          ← Firebase initialization
│           ├── App.jsx              ← Root component + auth state
│           ├── components/
│           │   ├── SocraticChat.jsx ← Main chat interface
│           │   ├── MathEditor.jsx   ← Math input with symbol palette
│           │   ├── KnowledgeMap.jsx ← Visual concept understanding map
│           │   └── ImageUpload.jsx  ← Photo upload component
│           └── pages/
│               ├── Login.jsx
│               ├── Dashboard.jsx
│               └── Session.jsx
│
├── docker-compose.yml               ← Run entire stack with one command
└── README.md
```

---

## 18. Resume Bullet Points

Write these once the project is complete and deployed. Each one maps to a specific phase.

**Bullet 1 (Phase 2 + 4):**
Built a full-stack AI mathematics tutoring platform using FastAPI (Python) and React, implementing a Socratic dialogue system with Gemini 2.0 Flash that teaches ML mathematics through guided questioning rather than direct answers

**Bullet 2 (Phase 3):**
Engineered a symbolic mathematics engine using SymPy for exact algebraic computation, covering differentiation, integration, gradient computation, and eigendecomposition — guaranteeing mathematically correct answers for student verification

**Bullet 3 (Phase 4):**
Designed a misconception detection system using LLM classification that categorizes student understanding into five types (conceptual confusion, sign error, scope error, partial, correct) and routes Socratic dialogue accordingly

**Bullet 4 (Phase 7):**
Implemented a student knowledge tracking system using vector embeddings (Gemini text-embedding-004 + ChromaDB) that maps conceptual understanding across 10 ML mathematics topics and identifies specific misconceptions over time

**Bullet 5 (Phase 8):**
Built a mathematical OCR pipeline combining Pix2Tex and Gemini Vision to extract LaTeX from handwritten and printed math images, enabling users to photograph textbook problems and receive Socratic tutoring

**Bullet 6 (Phase 5 + 8):**
Designed a PostgreSQL database schema with JSONB columns for flexible misconception storage, implemented Firebase Authentication for secure user management, and deployed to Google Cloud Run + Firebase Hosting at zero cost

---

## 19. Quick Reference — Commands Cheat Sheet

### Python / Virtual Environment
```bash
python3 -m venv venv              # create venv
source venv/bin/activate           # activate (Mac/Linux)
deactivate                         # exit venv
pip install package_name           # install a package
pip freeze > requirements.txt      # save installed packages
pip install -r requirements.txt    # restore from saved list
```

### FastAPI
```bash
uvicorn main:app --reload          # start development server
# Visit: localhost:8000/docs       interactive API documentation
```

### Git
```bash
git add .                          # stage all changes
git commit -m "message"            # save snapshot
git push                           # upload to GitHub
git status                         # see what changed
git log --oneline                  # see commit history
git diff                           # see exact changes
```

### Docker
```bash
docker compose up                  # start all services
docker compose up -d               # start in background
docker compose down                # stop all services
docker compose logs backend        # see backend logs
```

### Google Cloud
```bash
gcloud auth login                  # authenticate
gcloud config set project ID       # set active project
gcloud run deploy NAME --source .  # deploy to Cloud Run
firebase deploy                    # deploy frontend
```

### PostgreSQL (local development)
```bash
sudo systemctl start postgresql    # start PostgreSQL on Pop!_OS
psql -U postgres                   # open PostgreSQL terminal
\l                                  # list databases
\c socratic_tutor                  # connect to database
\dt                                 # list tables
\q                                  # quit
```

### Redis (local development)
```bash
sudo apt install redis-server      # install
redis-server                       # start
redis-cli ping                     # test (should return PONG)
```

### Testing your API from terminal (httpie)
```bash
# GET request
http localhost:8000/health

# POST request with JSON body
http POST localhost:8000/api/ask \
  question="What is backpropagation?" \
  topic="backprop"
```

---

## Key Principles to Never Forget

1. **The tutor never answers directly.** If you are writing code that makes the AI give the answer before the student has reasoned, something is wrong with the prompt.

2. **SymPy for correctness, Gemini for reasoning.** SymPy always knows the correct answer. Gemini knows how to teach it. They work together — neither alone is enough.

3. **One question per response.** The system prompt must enforce this. Two questions overwhelms the student and breaks the Socratic flow.

4. **Misconception detection is the product's core value.** Any tool can give an answer. Only this one diagnoses *why* you are wrong and adapts the dialogue to fix it.

5. **Commit after every working feature.** `git add . && git commit -m "message"` takes 10 seconds. It saves hours of recovery work.

6. **Test in Colab before writing production code.** Prototype every new library or API in a Colab notebook. Only move it into your backend once it works.

7. **The milestone defines done.** Each phase has one sentence that tells you when it is complete. Do not move forward until that sentence is true.

---

*This document was generated from the full planning conversation between Vishruth and Claude (April 2026). Update it as the project evolves.*
