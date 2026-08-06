from turtle import Screen
from food import Food
from snake import Snake
from scroreboard import Scoreboard
import time


# -------------------------------
# Game window configuration
# -------------------------------
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# -------------------------------
# Create the main game objects
# -------------------------------
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# -------------------------------
# Keyboard controls
# The Screen object listens for key presses
# and tells the Snake object to change direction.
# -------------------------------
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game = True
while game:
    # Refresh the screen manually because tracer(0)
    # disables automatic screen updates.
    screen.update()
    time.sleep(0.1)

    # Move the snake one step forward.
    snake.move()

    # -------------------------------
    # Food collision
    # When the snake reaches the food:
    # - Move the food to a new random position.
    # - Extend the snake's body.
    # - Increase the player's score.
    # -------------------------------
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # -------------------------------
    # Wall collision
    # End the game if the snake moves
    # outside the game boundaries.
    # -------------------------------
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        scoreboard.game_over()
        game = False

    # -------------------------------
    # Tail collision
    # Skip the head (index 0) and check
    # whether the head touches any body segment.
    # -------------------------------
    for segmente in snake.new_shape[1:]:
        if snake.head.distance(segmente) < 10:
            game = False
            scoreboard.game_over()

screen.exitonclick()