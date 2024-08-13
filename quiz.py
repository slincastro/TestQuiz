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
    while questions:
        question = random.choice(questions)
        correct = ask_question(question)
        if correct:
            print("-"*20+"\n")
            print("Correct!\n")
            print("-"*20)
        else:
            print("X" * 40 + "\n")
            print(f"Incorrect! The correct answer was {question['correct']}.\n")
            print("X"*40)
        
        questions.remove(question)

    print("You've completed the quiz!")

if __name__ == "__main__":
    quiz()
