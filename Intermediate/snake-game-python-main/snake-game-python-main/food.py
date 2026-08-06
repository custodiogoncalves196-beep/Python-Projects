from turtle import Turtle
import random

class Food(Turtle):
    """
    Food Class

    Purpose:
        Represents the food that the snake eats.

    Inheritance:
        Inherits from the Turtle class to reuse its graphical
        features such as shape, color, movement and positioning.

    Responsibilities:
        - Display the food on the screen.
        - Move to a random location after being eaten.
    """

    def __init__(self):
        # Initialize the parent Turtle class.
        super().__init__()

        # Configure the food's appearance.
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        # Place the food at a random starting position.
        self.refresh()

    def refresh(self):
        """
        Move the food to a new random position inside the game area.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)