from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from model import generate_answer
import uvicorn

app = FastAPI()

@app.post("/api/")
async def answer_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    image = data.get("image")  # Optional, if you want to support images later
    result = generate_answer(question, image)
    return JSONResponse(content=result)

# Mount static files from the 'static' directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Optional: Redirect root URL to /index.html
@app.get("/")
def root():
    return RedirectResponse("/index.html")

# Run locally
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
