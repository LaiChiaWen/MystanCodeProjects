"""
File: draw_line.py
Name: 賴珈汶
-------------------------
TODO:This program create one circle at the first click, and one line
will show at the second click. However, the circle will disappear.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 10
count = 1
window = GWindow()
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(mouse):
    """
    The user clicks the first time, the window will show a circle.
    And the user clicks the second time, circle will disappear and show one line.
    """
    global count
    global x1
    global y1
    if count % 2 == 1:
        x1 = mouse.x - SIZE / 2
        y1 = mouse.y - SIZE / 2
        hole_site = GOval(SIZE, SIZE, x=x1, y=y1)
        window.add(hole_site)
        count += 1
    else:
        old_hole = window.get_object_at(x1+SIZE/2, y1+SIZE/2)
        window.remove(old_hole)
        line = GLine(x1, y1, mouse.x, mouse.y)
        window.add(line)
        count += 1


if __name__ == "__main__":
    main()
