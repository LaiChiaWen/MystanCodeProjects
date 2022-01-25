"""
File: bouncing_ball.py
Name: 賴珈汶
-------------------------
TODO: When the user clicks, the ball will fall and bounce.
While the ball reaches the right wall, the ball will come back to the initial site.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
OVER_WINDOW = 3
over_window = 0

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window.add(ball)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(move)


def move(mouse):
    """
    The ball falls and bounces when clicking. When it reaches the
    window, it will come back to the initial state.
    """
    vy = 0
    global over_window
    ball_at_start = window.get_object_at(START_Y, START_Y)
    if ball_at_start is not None and over_window < OVER_WINDOW:
        while True:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y+ball.height >= window.height:
                vy = -vy * REDUCE
            pause(DELAY)
            if ball.x >= window.width:
                ball.x = START_X
                ball.y = START_Y
                over_window += 1
                break


if __name__ == "__main__":
    main()
