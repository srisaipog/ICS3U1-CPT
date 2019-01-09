"""
Connect the Dots
Sridhar Sairam
"""

# Global Variables

# Dots and Coordinates

position = []
pos_index = 0
dots = []
lines = []
p1_lines = []
p2_lines = []
temp_line = []

player_1_boxes = []
player_2_boxes = []

# Global CONSTANTS
DOT_SIZE = 10

# Key Codes
KEY_UP = 38
KEY_DOWN = 40
KEY_LEFT = 37
KEY_RIGHT = 39
KEY_ENTER = 10
KEY_SPACE = 32
KEY_R = 82

# Length and Width of Dots
GRID_LEN = 8
GRID_WID = 8

# Colours
BACKGROUND_COLOUR = (255, 255, 255)
CURSOR_COLOUR = (255, 0, 0)
DOT_COLOUR = (0, 0, 0)
SELECTION_COLOUR = (0, 255, 0)
SELECTABLE_COLOUR = (0, 0, 255)

# Line Colours
PLAYER_1_COLOUR = (255, 255, 0)
PLAYER_2_COLOUR = (255, 51, 153)

# ET CETERA
LINE_DIS_1 = 0
LINE_DIS_2 = 0

selection = False
bad_line = False
turn = "p1"


def setup():
    # Importing Global Variables
    global position, dots, pos_index
    global LINE_DIS_1, LINE_DIS_2

    # Setting background colour
    background(BACKGROUND_COLOUR[0], BACKGROUND_COLOUR[1], BACKGROUND_COLOUR[2])

    # Setting size of screen
    size(480, 640)

    # Creating array (list) of dots
    for j in range(GRID_LEN):
        for i in range(GRID_WID):
            x = i * (height / 10) + 15
            y = j * (width / 10) + 75
            dots.append([x, y])

    pos_index = 0
    position = dots[pos_index]

    LINE_DIS_1 = sqrt(((dots[0][0] - dots[1][0]) ** 2) +
                      ((dots[0][1] - dots[1][1]) ** 2))

    LINE_DIS_2 = sqrt(((dots[0][0] - dots[GRID_WID][0]) ** 2) +
                      ((dots[GRID_WID][1] - dots[1][1]) ** 2))

    # print("Number of Dots: " + str(len(dots)))
    # print("Distance Between 2 Dots (1) = " + str(LINE_DIS_1))
    # print("Distance Between 2 Dots (2) = " + str(LINE_DIS_2))

    # player_1_boxes.append(dots[5])
    # print(dots)

    # print((LINE_DIS_2), (LINE_DIS_1))


def draw():
    # Background
    background(BACKGROUND_COLOUR[0], BACKGROUND_COLOUR[1], BACKGROUND_COLOUR[2])
    
    boxx = makes_box(dots, lines)
    
    # print(lines)

    if boxx == False:
        print("How did u get here?")
    else:
        if turn == "p1":
            if boxx not in player_1_boxes:
                player_1_boxes.append(boxx)
        elif turn == "p2":
            if boxx not in player_2_boxes:
                player_2_boxes.append(boxx)

    print("p1", player_1_boxes)
    
    print("p2", player_2_boxes)

    # Drawing the Rectangles
    
    noStroke()
    
    fill(PLAYER_1_COLOUR[0], PLAYER_1_COLOUR[1], PLAYER_1_COLOUR[2])
    for dabba in player_1_boxes:
        rect(dabba[0], dabba[1], (LINE_DIS_1), (LINE_DIS_2))

    fill(PLAYER_2_COLOUR[0], PLAYER_2_COLOUR[1], PLAYER_2_COLOUR[2])
    for dabba in player_2_boxes:
        rect(dabba[0], dabba[1], (LINE_DIS_1), (LINE_DIS_2))

    # Setting attributes of dots
    fill(DOT_COLOUR[0], DOT_COLOUR[1], DOT_COLOUR[2])
    strokeWeight(0)

    # Drawing dots
    for dot in dots:
        ellipse(dot[0], dot[1], DOT_SIZE, DOT_SIZE)

    # Setting color of position cursor and drawing cursor
    if selection:
        fill(SELECTION_COLOUR[0], SELECTION_COLOUR[1], SELECTION_COLOUR[2])
    else:
        fill(CURSOR_COLOUR[0], CURSOR_COLOUR[1], CURSOR_COLOUR[2])

    ellipse(position[0], position[1], DOT_SIZE, DOT_SIZE)

    # Drawing Cursor
    fill(SELECTABLE_COLOUR[0], SELECTABLE_COLOUR[2], SELECTABLE_COLOUR[2])
    if selection:
        ellipse(temp_line[0][0], temp_line[0][1], DOT_SIZE, DOT_SIZE)

        temp_dis = sqrt(((position[0] - temp_line[0][0]) ** 2) +
                        ((position[1] - temp_line[0][1]) ** 2))

        strokeWeight(01)

        if (temp_dis == LINE_DIS_1 or
           temp_dis == LINE_DIS_2):
            stroke(0, 250, 0)
        else:
            stroke(255, 0, 0)

        line(position[0], position[1], temp_line[0][0], temp_line[0][1])

        # print(temp_dis, LINE_DIS_1, LINE_DIS_2)

    strokeWeight(width/100)

    # Drawing Player Lines
    for write in p1_lines:
        stroke(PLAYER_1_COLOUR[0], PLAYER_1_COLOUR[1], PLAYER_1_COLOUR[2])
        line(write[0][0], write[0][1], write[1][0], write[1][1])

    for write in p2_lines:
        stroke(PLAYER_2_COLOUR[0], PLAYER_2_COLOUR[1], PLAYER_2_COLOUR[2])
        line(write[0][0], write[0][1], write[1][0], write[1][1])

    # Writing Who's Turn It Is
    fill(255, 0, 0)
    if turn == "p1":
        textSize((width + height)//25)
        text("Player 1", width/2 - width/9, height/15)
    elif turn == "p2":
        textSize((width + height)//25)
        text("Player 2", width/2 - width/9, height/15)

    # Telling the player if they are a noob
    if bad_line:
        text("Please put a proper line", 10, height)


def makes_box(dotz, linez):
    
    """
    lin 1
    lin 2
    lin 3
    lin 4
    
    dot = top left of square
    
    square abcd
    
    a = (dotx, doty)
    b = (dotx, doty - vert len)
    c = (dotx + hor len, doty - ver len)
    d = (dotx + hor len, dot y)
    
    
    if
    lin 1 = a, b
    lin 2 = b, c
    lin 3 = c, d
    lin 4 = d, a
    
    """
    return box_cor


def keyPressed():
    # Importing Global Variables
    global position, dots, pos_index, selection
    global LINE_DIS_1, LINE_DIS_2, temp_line, turn, bad_line

    # Moving the cursor position
    # depending on key pressed

    # Moving Up
    if keyCode == KEY_UP:
        # print("UP")

        pos_index -= GRID_LEN

        if pos_index < 0:
            pos_index += GRID_LEN * GRID_WID

        position = dots[pos_index]

    # Moving Down
    elif keyCode == KEY_DOWN:
        # print("DOWN")

        pos_index += GRID_LEN

        try:
            position = dots[pos_index]
        except:
            pos_index -= GRID_LEN * GRID_WID
        finally:
            position = dots[pos_index]

    # Moving Left
    elif keyCode == KEY_LEFT:
        # print("LEFT")

        pos_index -= 1

        if ((pos_index + 1) % GRID_WID == 0 or
           pos_index == -1):
            pos_index += GRID_WID

        position = dots[pos_index]

    # Moving Right
    elif keyCode == KEY_RIGHT:
        # print("RIGHT")

        pos_index += 1

        if pos_index % (GRID_WID) == 0:
            pos_index -= (GRID_WID)

        position = dots[pos_index]

    # Selecting a dot
    elif (keyCode == KEY_ENTER or
          keyCode == KEY_SPACE):

        if not selection:

            temp_line = [position]

            selection = True
        elif selection:

            temp_line += [position]

            # print(temp_line)

            distance = sqrt(((temp_line[0][0] - temp_line[1][0]) **
                            2) + ((temp_line[0][1] - temp_line[1][1]) ** 2))

            if (temp_line in lines) or (temp_line[::-1] in lines):
                equivalent = True
            else:
                equivalent = False

            proper_distance = ((distance == LINE_DIS_1) or
                               (distance == LINE_DIS_2))

            add_line = proper_distance and not(equivalent)

            if add_line:
                bad_line = False
                if turn == "p1":
                    p1_lines.append(temp_line)
                    turn = "p2"
                elif turn == "p2":
                    p2_lines.append(temp_line)
                    turn = "p1"
                lines.append(temp_line)
            else:
                bad_line = True

            selection = False

            # print(str(equivalent))

            # print(lines)
