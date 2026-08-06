from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    """
    Scoreboard Class

    Purpose:
        Keeps track of the player's score and displays
        game-related messages on the screen.

    Inheritance:
        Inherits from the Turtle class to reuse its
        text writing and positioning capabilities.

    Stores:
        - Current score.

    Responsibilities:
        - Display the current score.
        - Update the score after the snake eats food.
        - Display the Game Over message.
    """

    def __init__(self):
        # Initialize the parent Turtle class.
        super().__init__()

        # Configure the scoreboard.
        self.score = 0
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.hideturtle()

        # Display the initial score.
        self.update_score()

    def update_score(self):
        """
        Display the current score on the screen.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Display the Game Over message in the center of the screen.
        """
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase the score and refresh the scoreboard.
        """
        self.score += 1

        # Remove the previous score before writing the new one.
        self.clear()
        self.update_score()