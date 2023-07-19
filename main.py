from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.snake_head.distance(food) < 20:
        food.food_position()
        snake.snake_eating()
        score.add_score()

    #Detect collision with wall
    if snake.snake_head.xcor() >= 290 or snake.snake_head.xcor() <= -290 or snake.snake_head.ycor() >= 290 or snake.snake_head.ycor() <= -290:
        game_is_on = False
        score.gameover()

    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.snake_head.distance(seg) < 10:
            game_is_on = False
            score.gameover()


screen.exitonclick()