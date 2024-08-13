import random
import json

# Load the questions from the JSON file
with open('questions.json', 'r') as file:
    questions = json.load(file)

# Function to ask a question
def ask_question(q):
    print(q["Question"])
    print(f"a) {q['a']}")
    print(f"b) {q['b']}")
    print(f"c) {q['c']}")
    print(f"d) {q['d']}\n")
    answer = input("Please select an option (a, b, c, d): ").strip().lower()
    return answer == q["correct"]

# Main loop
def quiz():
    while questions:
        question = random.choice(questions)
        correct = ask_question(question)
        if correct:
            print("-"*20+"\n")
            print("Correct!\n")
            print("-"*20)
        else:
            print("X"*20)
            print(f"Incorrect! The correct answer was {question['correct']}.\n")
            print("X"*20)
        
        # Remove the question from the list
        questions.remove(question)

    print("You've completed the quiz!")

if __name__ == "__main__":
    quiz()
