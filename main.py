from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

from model import answer_question

app = FastAPI(title="TDS Virtual TA API")

# Define the request schema
class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None  # currently unused

# Define the response schema
class AnswerResponse(BaseModel):
    answer: str
    references: List[str]

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    # Extract question from request
    question_text = request.question.strip()
    
    # Get answer using your model logic
    answer, refs = answer_question(question_text)
    
    # Return structured response
    return AnswerResponse(answer=answer, references=refs)

# Optional: For running directly with python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
