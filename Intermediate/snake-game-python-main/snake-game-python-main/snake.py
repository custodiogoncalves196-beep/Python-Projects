from turtle import Turtle

POSITIONS_STAR = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180



class Snake:
    """
    Snake Class

    Purpose:
        Represents the snake in the game.

    Stores:
        - All body segments.
        - A reference to the snake's head.

    Responsibilities:
        - Create the snake.
        - Move the snake.
        - Grow after eating food.
        - Change movement direction.
    """

    def __init__(self):
        # Store all snake body segments.
        self.new_shape = []

        # Create the initial snake.
        self.create_snake()

        # Keep a direct reference to the head for easier access.
        self.head = self.new_shape[0]

    def create_snake(self):
        """
        Create the snake using the predefined starting positions.
        """
        for position in POSITIONS_STAR:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Create a new body segment and add it to the snake.
        """
        snake = Turtle(shape="square")
        snake.color("white")
        snake.up()
        snake.goto(position)
        self.new_shape.append(snake)

    def extend_snake(self):
        """
        Add a new segment at the position of the last segment,
        making the snake grow.
        """
        self.add_segment(self.new_shape[-1].position())

    def move(self):
        """
        Move the snake by updating each body segment from
        tail to head, then move the head forward.
        """
        for shape in range(len(self.new_shape) - 1, 0, -1):
            new_x = self.new_shape[shape - 1].xcor()
            new_y = self.new_shape[shape - 1].ycor()
            self.new_shape[shape].goto(new_x, new_y)

        self.new_shape[0].forward(MOVE_DISTANCE)

    def up(self):
        """Change the snake's direction to up."""
        self.new_shape[0].setheading(UP)

    def down(self):
        """Change the snake's direction to down."""
        self.new_shape[0].setheading(DOWN)

    def left(self):
        """Change the snake's direction to the left."""
        self.new_shape[0].setheading(LEFT)

    def right(self):
        """Change the snake's direction to the right."""
        self.new_shape[0].setheading(RIGHT)