from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game 2022")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

should_game = True

while should_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

    # detect collision with wall.
    if snake.head.xcor() > 200 or snake.head.xcor() <-200\
            or snake.head.ycor() > 200 or snake.head.ycor()<-200:
        should_game = False
        scoreboard.game_over()

    # detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            should_game = False
            scoreboard.game_over()

screen.exitonclick()
