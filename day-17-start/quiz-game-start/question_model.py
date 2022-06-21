from mimetypes import init


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


if __name__ == "__main__":
    new_que = Question("question_text", "question_answer")
    print(new_que.text)