import random

class Question:
    def __init__(self, question: str, choices: list, answer: str):
        if not isinstance(question, str):
            raise ValueError("La question doit être une chaîne de caractères")
        self.question = question

        if len(choices) != 3:
            raise ValueError("Il faut 3 choix")
        self.choices = choices

        if not isinstance(answer, str):
            raise ValueError("La réponse doit être un nombre")
        if answer not in ["A","a","B","b","C","c"]:
            raise ValueError("La réponse doit être A, B ou C")
        self.shuffle_choices(answer)

    def get_question(self):
        return self.question
    
    def get_choices(self):
        return self.choices

    def get_answer(self):
        return self.answer

    def shuffle_choices(self, answer_letter: str):
        answer: list = self.choices[ord(answer_letter.lower()) - 97]
        random.shuffle(self.choices)
        self.answer = chr(97 + self.choices.index(answer))