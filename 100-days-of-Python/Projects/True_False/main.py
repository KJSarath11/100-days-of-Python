from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(Q_text=question_text,Q_answer=question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")