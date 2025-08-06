import os
import requests

DEEPAI_API_KEY = os.getenv("DEEPAI_API_KEY")

def generate_answer(question: str):
    url = "https://api.deepai.org/api/text-generator"
    headers = {
        "api-key": DEEPAI_API_KEY
    }
    data = {'text': question}
    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        answer = result.get("output", "Sorry, no answer generated.")
        return {
            "answer": answer,
            "links": [{"url": "https://deepai.org/machine-learning-model/text-generator", "text": "DeepAI Text Generator"}]
        }
    else:
        return {
            "answer": f"Error generating answer: {response.text}",
            "links": [{"url": "https://deepai.org/machine-learning-model/text-generator", "text": "DeepAI Text Generator"}]
        }
