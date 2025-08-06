from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from model import generate_answer  # Adjust if your AI function is in model.py

app = FastAPI()

# Define the API route BEFORE mounting static files
@app.post("/api/")
async def answer_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    result = generate_answer(question)
    return JSONResponse(content=result)

@app.get("/")
def root():
    return RedirectResponse("/index.html")

# Mount static files at root (serves your index.html and other static files)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
