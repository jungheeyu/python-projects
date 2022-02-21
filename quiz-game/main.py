import data
from question_model import Question
from quiz_brain import QuizBrain

play = True
while play:
    question_data = ""
    question_bank = []

    category = input("Choose your quiz category: (n: Nature, m: Math, c: Computer)   ")

    if category == "n":
        question_data = data.nature_question_data
    elif category == "m":
        question_data = data.math_question_data
    elif category == "c":
        question_data = data.computer_question_data
    else:
        question_data = data.random_question_data

    for q_data in question_data:
        question_text = q_data["question"]
        question_answer = q_data["correct_answer"]
        new_question = Question(question_text,question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_question():
        quiz.next_question()

    print("You've completed the quiz!")
    print(f"Your final score is {quiz.score}/{quiz.question_number}\n")
    play = True if input("Do you want to play Quiz Game? (y: Yes, n: No)   ") == "y" else False
    print("")

print("Good Bye!!")