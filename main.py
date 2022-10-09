import requests
from question import Question
from QuizBrain import quizbrain

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_data = response.json()['results']
question_bank = []
for question in question_data:
    question_text = question['question']
    question_ans = question['correct_answer']
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = quizbrain(question_bank)
end = False
while not end:
    quiz.new_question()
