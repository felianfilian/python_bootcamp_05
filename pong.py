from turtle import Screen
from pong_paddle import Paddle

def start():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    # screen.tracer(0)
    #
    # r_paddle = Paddle((350, 0))
    # l_paddle = Paddle(-350, 0)
    #
    # screen.listen()
    # screen.onkey(l_paddle.go_up(), "w")
    # screen.onkey(l_paddle.go_up(), "s")
    # screen.onkey(r_paddle.go_up(), "UP")
    # screen.onkey(r_paddle.go_up(), "DOWN")
    #
    # game_active = True
    # while game_active:
    #     screen.update()

    screen.exitonclick()
