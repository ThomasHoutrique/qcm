class question:
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
        self.answer = answer

    def get_question(self):
        return self.question
    
    def get_choices(self):
        return self.choices

    def get_answer(self):
        return self.answer