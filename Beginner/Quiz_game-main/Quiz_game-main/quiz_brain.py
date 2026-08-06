class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        correct_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {correct_question.question} (True/False)")
        self.check_answer(user_answer, correct_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"Te correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")






