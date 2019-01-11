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
CURSOR_SIZE = 15

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
CURSOR_COLOUR_P1 = (255, 0, 0)
CURSOR_COLOUR_P2 = (255, 100, 0)
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
    
    import random
    
    # Importing Global Variables
    global position, dots, pos_index
    global LINE_DIS_1, LINE_DIS_2

    # Setting background colour
    background(BACKGROUND_COLOUR[0],
               BACKGROUND_COLOUR[1],
               BACKGROUND_COLOUR[2])

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
    
    # Assert functions when game starts
    if frameCount < 300:
        tests(lines, dots)

    global turn
    # Background
    background(BACKGROUND_COLOUR[0],
               BACKGROUND_COLOUR[1],
               BACKGROUND_COLOUR[2])

    boxes = makes_box(dots, lines)

    # print(lines)
    
    temp = False
    
    if boxes:
        for boxx in boxes:
            if turn == "p2":
                if (boxx not in player_1_boxes and boxx not in player_2_boxes):
                    player_1_boxes.append(boxx)
                    temp = True
            elif turn == "p1":
                if (boxx not in player_2_boxes and boxx not in player_1_boxes):
                    player_2_boxes.append(boxx)
                    temp = True
    if temp and turn == "p1":
        turn = "p2"
    elif temp and turn == "p2":
        turn = "p1"

    # print("p1", player_1_boxes)
    # print("p2", player_2_boxes)

    # Drawing the Rectangles

    noStroke()

    fill(PLAYER_1_COLOUR[0], PLAYER_1_COLOUR[1], PLAYER_1_COLOUR[2])
    for dabba in player_1_boxes:
        rect(dabba[0] + (LINE_DIS_1/6.4), dabba[1] + (LINE_DIS_1/6.4),
             (LINE_DIS_1) - (LINE_DIS_1/3.2), (LINE_DIS_2) - (LINE_DIS_2/2.4))

    fill(PLAYER_2_COLOUR[0], PLAYER_2_COLOUR[1], PLAYER_2_COLOUR[2])
    for dabba in player_2_boxes:
        rect(dabba[0] + (LINE_DIS_1/6.4), dabba[1] + (LINE_DIS_1/6.4),
             (LINE_DIS_1) - (LINE_DIS_1/3.2), (LINE_DIS_2) - (LINE_DIS_2/2.4))

    fill(255, 0, 0)
    textSize(15)
    text("Points:", 10, 30)

    textSize(20)

    fill(PLAYER_2_COLOUR[0], PLAYER_2_COLOUR[1], PLAYER_2_COLOUR[2])
    text("P2: " + str((len(player_2_boxes))), 75, 50)

    fill(PLAYER_1_COLOUR[0], PLAYER_1_COLOUR[1], PLAYER_1_COLOUR[2])
    text("P1: " + str((len(player_1_boxes))), 75, 25)

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
        if turn == "p1":
            fill(CURSOR_COLOUR_P1[0], CURSOR_COLOUR_P1[1], CURSOR_COLOUR_P1[2])
        elif turn == "p2":
            fill(CURSOR_COLOUR_P2[0], CURSOR_COLOUR_P2[1], CURSOR_COLOUR_P2[2])

    ellipse(position[0], position[1], CURSOR_SIZE, CURSOR_SIZE)

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
        textSize(30)
        text((turn.upper() + ", Please put a proper line"), 50, height - 50)
    
    if end_game(GRID_WID, GRID_LEN, player_1_boxes, player_2_boxes):
        background(0)
        p1_score = len(player_1_boxes)
        p2_score = len(player_2_boxes)
        
        if p1_score > p2_score:
            win = "Player 1"
        elif p1_score < p2_score:
            win = "Player 1"
        else:
            win = "Draw"

        textSize(30)
            
        if win != "Draw":
            text((win, "has won!"), 100, 50)
        else:
            text("It's a draw!", 100, 50)
        
        text(("P1: " + str(p1_score)), 100, 100)
        text(("P2: " + str(p2_score)), 200, 100)


def tests(lines, dots):
    for linee in lines:
        assert linee[0] in dots, "rouge line detected"
        assert linee[1] in dots, "illegal line has crossed the border"
    
    assert position in dots, "you're off the tracks"


def end_game(wid, leng, p1_box, p2_box):
    total_boxes = wid * leng
    cur_boxes = len(p1_box) + len(p2_box)

    if total_boxes == cur_boxes:
        return True
    else:
        return False


def makes_box(dots, lines):

    box_cors = []

    for dott in dots:
        a = [dott[0], dott[1]]
        b = [dott[0], dott[1] + LINE_DIS_2]
        c = [dott[0] + LINE_DIS_1, dott[1] + LINE_DIS_2]
        d = [dott[0] + LINE_DIS_1, dott[1]]

        lin_1 = [a, b]
        lin_2 = [b, c]
        lin_3 = [c, d]
        lin_4 = [d, a]

        lines_1_to_4 = [lin_1, lin_2, lin_3, lin_4]

        lines_out_of_4 = 0
        for lin_1_4 in lines_1_to_4:
            for lin in lines:
                if (lin[0] in lin_1_4 and lin[1] in lin_1_4):
                    lines_out_of_4 += 1
                    # (lines_out_of_4)

                if lines_out_of_4 == 4:
                    box_cors.append(a)
                    # print(box_cors)

    if len(box_cors) >= 1:
        # print(box_cors)
        return box_cors


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
