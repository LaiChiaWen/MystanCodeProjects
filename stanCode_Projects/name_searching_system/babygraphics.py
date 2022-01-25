"""
File: babygraphics.py
Name: 賴珈汶
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    inner_width = width - 2 * GRAPH_MARGIN_SIZE
    column_width = inner_width / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * column_width
    return x_coordinate


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    inner_height = height - 2 * GRAPH_MARGIN_SIZE
    y_coordinate = GRAPH_MARGIN_SIZE + int(rank) * (inner_height / MAX_RANK)
    return y_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    top_line = canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                                  CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    down_line = canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        line_i = canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i),
                                    CANVAS_HEIGHT, width=LINE_WIDTH)
        text_i = canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                    text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    for i in range(len(lookup_names)):
        name = name_data[lookup_names[i]]   # dict, { year : rank }
        # color change
        if i % len(COLORS) == 0:
            color = COLORS[0]
        elif i % len(COLORS) == 1:
            color = COLORS[1]
        elif i % len(COLORS) == 2:
            color = COLORS[2]
        else:
            color = COLORS[3]

        # decides the YEARS[j] is in name or not, and draws the name and rank on the canvas
        y = []  # List(str), the ranks in years
        for j in range(len(YEARS)):
            if str(YEARS[j]) in name:
                rank_j = name[str(YEARS[j])]
                y.append(rank_j)
                show_name_1 = lookup_names[i] + " " + rank_j
                name_j = canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, j),
                                            get_y_coordinate(CANVAS_HEIGHT, rank_j),
                                            text=show_name_1, anchor=tkinter.SW, fill=color)
            else:
                show_name_2 = lookup_names[i] + " *"
                y.append(str(MAX_RANK))
                name_j = canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, j),
                                            CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                            text=show_name_2, anchor=tkinter.SW, fill=color)

        # draws the lines in years
        for k in range(len(YEARS)-1):
            start_x = get_x_coordinate(CANVAS_WIDTH, k)         # The position x in this year
            end_x = get_x_coordinate(CANVAS_WIDTH, k+1)         # The position x in next year
            start_y = get_y_coordinate(CANVAS_HEIGHT, y[k])     # The position y in this year
            end_y = get_y_coordinate(CANVAS_HEIGHT, y[k+1])     # The position y in next year
            line_k = canvas.create_line(start_x, start_y, end_x, end_y, width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
