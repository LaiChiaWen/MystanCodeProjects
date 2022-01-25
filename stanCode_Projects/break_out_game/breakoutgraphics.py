"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.

is_moving = False      # Control the ball moving.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.b_c = brick_cols
        self.b_r = brick_rows
        self.b_w = brick_width
        self.b_h = brick_height
        self.b_s = brick_spacing
        self.b_of = brick_offset
        self.p_of = paddle_offset
        self.ball_r = ball_radius
        self.no_restart = is_moving

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-(self.p_of+self
                                                                                                      .paddle.height))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # Draw bricks
        self.crate_bricks()

        # When win and print
        self.win = GLabel("You Win!", x=self.window.width/4, y=self.window.height/2)
        self.win.font = "-50"

        # When lose and print
        self.lose = GLabel("You lose", x=self.window.width/4, y=2*self.window.height/3)
        self.lose.font = "-50"

    def chang_y_way(self):
        """
        When the ball hit the bricks or paddle, change its y-axis direction
        """
        self.__dy = -self.__dy
        return self.__dy

    def touch_object(self):
        """
        To determine if the ball touches the object
        """
        left_up = self.window.get_object_at(self.ball.x, self.ball.y)
        left_down = self.window.get_object_at(self.ball.x, (self.ball.y+self.ball.height))
        right_up = self.window.get_object_at((self.ball.x+self.ball.width), self.ball.y)
        right_down = self.window.get_object_at((self.ball.x+self.ball.width), (self.ball.y+self.ball.height))
        if left_up is not None:
            return left_up
        elif left_down is not None:
            return left_down
        elif right_up is not None:
            return right_up
        elif right_down is not None:
            return right_down

    def ball_outside(self):
        """
        To determine if the ball goes out
        """
        is_ball_y_out_window = self.ball.y + self.ball.height > self.window.height
        return is_ball_y_out_window

    def ball_restart(self):
        """
        When ball goes out, reset the ball to the initial state
        """
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.no_restart = False
        self.__dx = 0

    def ball_move(self, mouse):
        """
        When click, the ball will move
        """
        if self.__dx == 0:
            self.no_restart = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        """
        When ball touch the window, change its x-axis speed
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        return self.__dx

    def get_dy(self):
        """
        When ball touch the window, change its y-axis speed
        """
        if self.ball.y <= 0 or self.ball.y + self.ball.height >= self.window.height:
            self.__dy = -self.__dy
        return self.__dy

    def paddle_move(self, mouse):
        """
        The paddle will move with the mouse
        """
        x1 = mouse.x - self.paddle.width/2
        y1 = self.window.height-(self.p_of+self.paddle.height)
        if mouse.x <= self.paddle.width/2:
            x1 = 0
        if mouse.x >= (self.window.width-self.paddle.width/2):
            x1 = self.window.width - self.paddle.width
        self.window.add(self.paddle, x=x1, y=y1)

    def crate_bricks(self):
        """
        This method crates bricks
        """
        for j in range(self.b_r):  # show a number of bricks in rows
            for i in range(self.b_c):  # show a number of bricks in columns
                self.brick_i = GRect(self.b_w, self.b_h)
                if j == 0 or j == 1:
                    color = "red"
                elif j == 2 or j == 3:
                    color = "orange"
                elif j == 4 or j == 5:
                    color = "yellow"
                elif j == 6 or j == 7:
                    color = "green"
                else:
                    color = "blue"
                self.brick_i.filled = True
                self.brick_i.fill_color = color
                self.brick_i.color = color
                self.window.add(self.brick_i, x=i*(self.brick_i.width+self.b_s), y=self.b_of+j*(self.b_h+self.b_s))


