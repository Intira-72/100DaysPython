import re


class QuizBrain:
    def __init__(self, quiz_list):
        self.quiz_number = 0
        self.quiz_list = quiz_list
        self.score = 0


    def still_has_quez(self):
        return len(self.quiz_list) > self.quiz_number


    def check_answer(self, u_answer, quiz_answer):
        if u_answer == quiz_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrang.")
        
        print(f'The correct answer was: {quiz_answer}')
        print(f'Your current score is: {self.score}/{self.quiz_number + 1}\n')


    def next_quiz(self):
        quiz = self.quiz_list[self.quiz_number]
        answer = input(f'Q.{self.quiz_number + 1} {quiz.text} (True/False)?: ')
        self.check_answer(answer.capitalize(), quiz.answer)
        self.quiz_number += 1


    



    
