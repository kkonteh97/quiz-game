class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        cur_q = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {cur_q.text} (True/false)?:")
        self.check_answer(user_ans, cur_q.answer)

    def still_has_question(self):
        return (self.question_number) < len(self.question_list)

    def check_answer(self, user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            self.score += 1
            print(f"you got it right! \nYour current score is: {self.score}/{self.question_number}.")

        else:
            print(f"that's wrong \nYour current score is: {self.score}/{self.question_number}.")
        print(f"the correct answer is: {corr_ans}.")
