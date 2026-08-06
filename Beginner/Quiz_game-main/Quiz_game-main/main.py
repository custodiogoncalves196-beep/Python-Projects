
# Import data and classes
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


# Create an empty list that will store Question objects
question_bank = []

# Loop through each dictionary inside question_data
for question in question_data:

    # Get the question text from the current dictionary
    question_text = question["question"]

    # Get the correct answer from the current dictionary
    question_answer = question["correct_answer"]

    """
    Create a Question object.

    This calls:
        __init__(self, question, answer)

    Python automatically does:

        __init__(new_question, question_text, question_answer)

    Inside the Question class:

        self.question = question
        self.answer = answer

    becomes:

        new_question.question = question_text
        new_question.answer = question_answer
    """

    new_question = Question(question_text, question_answer)

    # Add the Question object to the question bank
    question_bank.append(new_question)


"""
Create a QuizBrain object.

Python automatically calls:

    __init__(quiz, question_bank)

Inside QuizBrain:

    self.question_number = 0
    self.score = 0
    self.questions_list = q_list

where:

    q_list = question_bank

So the object stores:

    quiz.question_number = 0
    quiz.score = 0
    quiz.questions_list = question_bank
"""

quiz = QuizBrain(question_bank)


"""
Main game loop.

The loop continues while:

    quiz.still_has_question()

returns True.

Each iteration calls:

    quiz.next_question()

Inside next_question():

    1. Gets the current question
    2. Shows the question to the user
    3. Receives the user's answer
    4. Calls check_answer()
    5. Updates the score
"""

while quiz.still_has_question():
    quiz.next_question()


# Final message
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


## Flow of the Program

"""text
question_data
        ↓
for loop
        ↓
Question objects
        ↓
question_bank
        ↓
QuizBrain(question_bank)
        ↓
quiz object
        ↓
while quiz.still_has_question()
        ↓
quiz.next_question()
        ↓
check_answer()
        ↓
update score
        ↓
final score
"""







