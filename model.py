import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(question: str, image: str = None):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful Teaching Assistant for the Tools in Data Science course at IIT Madras."},
                {"role": "user", "content": question}
            ],
        )
        answer_text = response.choices[0].message.content.strip()
    except Exception as e:
        answer_text = f"Error generating answer: {e}"

    links = [{"url": "https://discourse.onlinedegree.iitm.ac.in", "text": "Discussion Forum"}]
    return {
        "answer": answer_text,
        "links": links
    }
