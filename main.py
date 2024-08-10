from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = ScoreBoard()
snake = Snake()
food = Food()
game_is_on = True

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.listen()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
   # print(snake.screem_limit())
   # print(snake.detect_coalition())

    if snake.screem_limit():# and not snake.detect_coalition():
        game_is_on = True
    else:
        game_is_on = False

    if game_is_on:
        if snake.detect_coalition2():  # and not snake.detect_coalition():
            game_is_on = False
        else:
            game_is_on = True


    if snake.head.distance(food) < 15:
        print(f"the distance -> {snake.head.distance(food)}")
        food.refresh()
        scoreboard.add_score()
        snake.extend_snake()

    if not game_is_on:
        scoreboard.game_over()

screen.exitonclick()
