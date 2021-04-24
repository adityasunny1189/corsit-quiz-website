import html


class QuizBrain:
    def __init__(self, question_bank):
        self.score = 0
        self.current_question = None
        self.question_number = 0
        self.question_list = question_bank

    def next_question(self):
        if self.question_number == 0:
            self.score = 0
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.question)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_ans):
        correct_ans = self.current_question.ans
        if correct_ans == user_ans:
            self.score += 1

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def reset(self):
        self.current_question = None
        self.question_number = 0
