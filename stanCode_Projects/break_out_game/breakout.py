"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    score = 0
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        # Win, when the score is equal to total bricks number
        if score == graphics.b_c * graphics.b_r:
            graphics.window.add(graphics.win)
            break

        # Lose, when the life is equal to 0
        if lives == 0:
            graphics.window.add(graphics.lose)
            break

        if graphics.no_restart and lives > 0:
            # Update
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            graphics.ball.move(vx, vy)

            # Bricks broken
            maybe_obj = graphics.touch_object()
            if maybe_obj is not None and maybe_obj is not graphics.paddle:
                graphics.window.remove(maybe_obj)
                graphics.chang_y_way()
                score += 1  # when break one brick, plus one
            # ball touch the paddle and doesn't stick on the paddle
            if maybe_obj is graphics.paddle and vy > 0:
                graphics.chang_y_way()

            # Outside and lose one life
            if graphics.ball_outside():
                graphics.ball_restart()
                lives -= 1
        # Pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
