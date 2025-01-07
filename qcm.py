from question import Question
import random
class QCM:
    def __init__(self, questions: list):
        self.questions = random.sample(questions, len(questions))
        self.index = 0
        self.score = 0

    def get_question(self):
        return self.questions[self.index].get_question()

    def get_choices(self):
        return self.questions[self.index].get_choices()

    def get_answer(self):
        return self.questions[self.index].get_answer()

    def next_question(self):
        self.index += 1

    def is_finished(self):
        return self.index == len(self.questions)

    def check_answer(self, answer: str):
        if answer not in ["A","a","B","b","C","c"]:
            raise ValueError("La réponse doit être A, B ou C")
        if answer == self.get_answer():
            self.score += 1
        self.next_question()

    def get_score(self):
        return self.score