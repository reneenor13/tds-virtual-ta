from fastapi import FastAPI, Request
from pydantic import BaseModel
from model import generate_answer

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: str | None = None

@app.post("/api/")
async def answer_question(req: QuestionRequest):
    response = generate_answer(req.question, req.image)
    return response
