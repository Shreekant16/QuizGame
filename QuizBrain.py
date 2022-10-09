class quizbrain:
    def __init__(self, ql):
        self.question_list = ql
        self.question_no = 0
        self.score = 0

    def new_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user = input(f"Q.{self.question_no} {current_question.question_text} (true/false) : ")
        self.check(user, current_question.question_ans)

    def check(self,given,correct):
        if given.lower() == correct.lower():
            self.score += 1
            print(f"You got it")
        else:
            print(f"That is wrong")

        print(f"{self.score}/{self.question_no}")

