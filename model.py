import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VirtualTA:
    def __init__(self, course_data: dict, discourse_data: dict):
        """
        Initialize the model with course and discourse content.
        """
        self.qa_pairs = self._prepare_qa_pairs(course_data, discourse_data)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.questions = [q for q, _ in self.qa_pairs]
        self.answers = [a for _, a in self.qa_pairs]
        self.tfidf_matrix = self.vectorizer.fit_transform(self.questions)

    def _prepare_qa_pairs(self, course_data, discourse_data):
        """
        Convert content into question-answer pairs. For now, we use simple title-content or question-answer.
        """
        qa_pairs = []
        for title, content in course_data.items():
            if content:
                qa_pairs.append((title, content))

        for post in discourse_data:
            question = post.get("title") or ""
            answer = post.get("content") or ""
            if question and answer:
                qa_pairs.append((question, answer))

        return qa_pairs

    def _clean_text(self, text):
        """
        Clean input text by lowering case and removing punctuation.
        """
        text = text.lower()
        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
        return text

    def answer_question(self, question: str, top_k: int = 1):
        """
        Return the most relevant answer to the input question.
        """
        cleaned_question = self._clean_text(question)
        q_vec = self.vectorizer.transform([cleaned_question])
        similarities = cosine_similarity(q_vec, self.tfidf_matrix).flatten()
        top_indices = similarities.argsort()[-top_k:][::-1]

        best_answers = []
        for idx in top_indices:
            score = similarities[idx]
            best_answers.append({
                "question": self.questions[idx],
                "answer": self.answers[idx],
                "score": round(float(score), 3)
            })

        return best_answers
