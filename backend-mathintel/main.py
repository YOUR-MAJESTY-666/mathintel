from fastapi import FastAPI

app = FastAPI(title="Socratic ML Tutor", version="0.1")

@app.get("/")
def root():
    return {"status": "alive", "message": "Socratic ML Tutor is running"}

@app.get("/health")
def health():
    return {"healthy": True}