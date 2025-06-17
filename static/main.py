from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

@app.post("/api/")
async def answer_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    return {"answer": f"You asked: {question}"}

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def root():
    return RedirectResponse("/index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
