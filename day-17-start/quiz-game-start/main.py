from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = [Question(i['text'], i['answer']) for i in question_data]


if __name__=="__main__":
    quiz = QuizBrain(question_bank)

    while quiz.still_has_quez():
        quiz.next_quiz()

    print("You've completed the quiz.")
    print(f'Your final score was: {quiz.score}/{quiz.quiz_number}')