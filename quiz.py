import random
import json

with open('questions.json', 'r') as file:
    questions = json.load(file)

def ask_question(q):
    
    print(q["Question"]+"\n")
    print(f"a) {q['a']}")
    print(f"b) {q['b']}")
    print(f"c) {q['c']}")
    print(f"d) {q['d']}\n")
    answer = input("Please select an option (a, b, c, d): ").strip().lower()
    return answer == q["correct"]


def quiz():
    correct_answers = 0

    while questions:
        question = random.choice(questions)
        print(f"\n Respuestas correctas: {correct_answers} \n")

        correct = ask_question(question)
        
        if correct:
            print("-"*20+"\n")
            print("Correct!\n")
            print("-"*20)
            correct_answers = correct_answers + 1
        else:
            print("X" * 90 + "\n")
            print(f"Incorrect! The correct answer was {question['correct']} :.\n")
            print(question["Question"]+"\n")
            print(f"{question[question['correct']]}\n")
            print("X" * 90)
            correct_answers =0
        
        questions.remove(question)

    print("You've completed the quiz!")

if __name__ == "__main__":
    
    quiz()
