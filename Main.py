import time
from turtle import Screen,Turtle
from snake import Snake  # ← importing your class
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("green")
screen.setup(width=600, height=600)
screen.tracer(0)

Font=("Arial",40,"bold",)

timmy=Turtle()
snake = Snake()
food=Food()
score=Score()
screen.listen()
timmy.hideturtle()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        score.score_count()
        snake.extend()

    if snake.head.xcor()>290 or snake.head.ycor()<-290 or snake.head.xcor()<-290 or snake.head.ycor()>290:
        timmy.write("Game over",move=False,align="center",font=Font)
        score.reset()
        game_is_on=False

    for segment in snake.segments:
        if snake.head.distance(segment)<15:
            if segment==snake.head:
                pass
            else:
                game_is_on=False
                score.reset()
                timmy.write("Game Over", font=Font)


screen.exitonclick()
