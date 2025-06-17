def generate_answer(question: str, image: str = None):
    links = [{"url": "https://discourse.onlinedegree.iitm.ac.in", "text": "Discussion Forum"}]
    return {
        "answer": f"Answering: {question}",
        "links": links
    }
