from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from analysis_agent import generate_answer  # Import your new AI function

app = FastAPI()

# Serve static files (like index.html)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.post("/api/")
async def answer_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    result = generate_answer(question)  # Call the AI function here
    return JSONResponse(content=result)

@app.get("/")
def root():
    return RedirectResponse("/index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
