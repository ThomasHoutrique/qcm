from qcm import QCM
from question import Question

q1: Question = question("Quelle est la capitale de la France ?", ["Paris", "Londres", "Berlin"], 'a')
q2: Question = question("Quelle est la capitale de l'Allemagne ?", ["Dublin", "Berlin", "Düsseldorf"], 'b')
q3: Question = question("Quelle est la capitale de l'Irlande ?", ["Dublin", "Londres", "Manchester"], 'a')
q4: Question = question("Quelle est la capitale de l'Italie ?", ["Rome", "Milan", "Naples"], 'a')
q5: Question = question("Quelle est la capitale des Émirats Arabes Unis ?", ["Dubaï", "Abu Dhabi", "Charjah"], 'b')
q6: Question = question("Quelle est la capitale des États-Unis ?", ["New York", "Washington DC", "Los Angeles"], 'b')
q7: Question = question("Quelle est la capitale de la Pologne ?", ["Cracovie", "Varsovie", "Gdańsk"], 'b')
q8: Question = question("Quelle est la capitale de la Russie ?", ["Saint-Pétersbourg", "Moscou", "Kazan"], 'b')
q9: Question = question("Quelle est la capitale du Japon ?", ["Osaka", "Tokyo", "Kyoto"], 'b')
q10: Question = Question("Quelle est la capitale de l'Australie ?", ["Sydney", "Canberra", "Melbourne"], 'b')

questions: list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

qcm: QCM = QCM(questions)

while not qcm.is_finished():
    print(qcm.get_question())
    for i, choice in enumerate(qcm.get_choices()):
        print(f"{chr(97 + i)}) {choice}")
    answer: str = input("Réponse: ")
    qcm.check_answer(answer)

print(f"Votre score est de {qcm.get_score()}/10")

print("Les réponses étaient:")
for i, question in enumerate(questions):
    print(f"{question.get_question()}: {question.get_answer()}")