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

select_cul = 0

colour_choice_1 = 1

colour_choice_2 = 2

# etc resettable

player_cul_choice = 0

colour_choice = 0
select_prev = 0
choice = "P1"

selection = False
bad_line = False
turn = "p1"

win = 0

prompt = False
menu_prompt = False

select = 1

# Global CONSTANTS
DOT_SIZE = 10

# Key Codes
KEY_UP = 38
KEY_DOWN = 40
KEY_LEFT = 37
KEY_RIGHT = 39
KEY_ENTER = 10
KEY_SPACE = 32

KEY_M = 77
KEY_Y = 89
KEY_N = 78
KEY_R = 82

# Length and Width of Dots
GRID_LEN = 8
GRID_WID = 8

CURSOR_SIZE = 15

# Colours
BACKGROUND_COLOUR = (255, 255, 255)
CURSOR_COLOUR = (255, 0, 0)
DOT_COLOUR = (0, 0, 0)
SELECTION_COLOUR = (0, 255, 0)
SELECTABLE_COLOUR = (0, 0, 255)

CURSOR_COLOUR_P1 = (255, 0, 0)
CURSOR_COLOUR_P2 = (255, 100, 0)

# Line Colours
PLAYER_1_COLOUR = (220, 20, 60)
PLAYER_2_COLOUR = (255, 140, 0)

# ET CETERA
LINE_DIS_1 = 0
LINE_DIS_2 = 0

OPTIONS = [[1, "Play"], [2, "Instructions"], [3, "Info"], [4, "Options"]]

state = "menu"


def setup():

    # print("setting up")

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

    # (LINE_DIS_2), (LINE_DIS_1))


def draw():

    global state, win, PLAYER_1_COLOUR, PLAYER_2_COLOUR, select, select_cul
    global colour_choice, selection, choice, prompt, menu_prompt
    global colour_choice_1, colour_choice_2, player_cul_choice

    # print(select)

    if state == "menu":
        # print(colour_choice, colour_choice_1, colour_choice_2)

        background(200)
        fill(255)
        stroke(0)
        strokeWeight(3)

        for i in range(1, 5):
            rect(width/2 - 100, 75 + (height/7) * i, (width/5)*2, (width/20)*2)

        fill(240, 230, 140)
        try:
            rect(width/2 - 100, 75 + (height/7) * select,
                 (width/5)*2, (width/20)*2)

            textSize(20)

            fill(0)

            for j in range(1, 5):
                text(OPTIONS[j-1][1], width/2 - 92, 100 + (height/7) * j)

            textSize(20)
            fill(0)
            text(("""     Use the ARROW KEYS to navigate and
            ENTER/SPACE KEYS to select"""),
                 width/2 - 200, height - 50)

        except:
            textSize(15)
            background(180)

            fill(44, 57, 142)

            if select == "Play":
                state = "game"
            elif select == "Instructions":
                text(instructions(), 5, 150)
            elif select == "Info":
                text(info(), 50, 150)
            elif select == "Options":

                stroke(20)

                colour_1 = (220, 20, 60)  # red
                colour_2 = (255, 140, 0)  # orange
                colour_3 = (255, 215, 0)  # yellow
                colour_4 = (50, 205, 50)  # green
                colour_5 = (30, 144, 255)  # blue
                colour_6 = (138, 43, 226)  # violet

                colours = [colour_1, colour_2, colour_3, colour_4,
                           colour_5, colour_6]

                p1_choice = PLAYER_1_COLOUR
                p2_choice = PLAYER_2_COLOUR

                for i, cul in enumerate(colours):
                    noStroke()
                    fill(cul[0], cul[1], cul[2])

                    rect(50 * (i + 1), 150, 50, 50)

                    textSize(20)
                    fill(255)
                    # text(str(i + 1), (50 * i) + 20 + 50, 140)

                if player_cul_choice == 1:
                    choice = "P1"
                elif player_cul_choice == 2:
                    choice = "P2"

                # print(p1_choice, p2_choice)

                if choice == "P1":
                    p1_choice = colours[colour_choice_1 - 1]
                elif choice == "P2":
                    p2_choice = colours[colour_choice_2 - 1]

                fill(255, 0)
                stroke(0)
                strokeWeight(5)
                rect(50 * (select_cul), 150, 50, 50)
                noStroke()
                fill(255)

                if choice == "P1":
                    textSize(25)
                else:
                    textSize(15)
                text("Player 1: ", 80, 300)

                if choice == "P2":
                    textSize(25)
                else:
                    textSize(15)
                text("Player 2: ", 80, 350)

                textSize(20)
                fill(0)
                text("""                 Use '1' and '2' to select colours for
                Player 1 and Player 2 respectively""", -30, height - 150)

                PLAYER_1_COLOUR = p1_choice
                PLAYER_2_COLOUR = p2_choice

                if p1_choice == p2_choice:
                    fill(255, 0, 0)
                    textSize(19)
                    text("CAUTION: Both players are using the same colour",
                         10, height - 230)
                    text("This may result in confusion during gameplay",
                         10, height - 200)
                    fill(0)

                fill(PLAYER_1_COLOUR[0],
                     PLAYER_1_COLOUR[1],
                     PLAYER_1_COLOUR[2])

                rect(200, 265, 50, 50)

                fill(PLAYER_2_COLOUR[0],
                     PLAYER_2_COLOUR[1],
                     PLAYER_2_COLOUR[2])

                rect(200, 315, 50, 50)

                # print(selection)
                # print(choice)

            textSize(20)
            fill(0)
            text("Press M to return to menu", 100, height - 50)

        fill(0)

        textSize(30)
        text("Connect The Dots", width/2 - 135, 40)

        textSize(25)
        if isinstance(select, int):
            menu_text = "Menu"
        else:
            menu_text = select

        text(menu_text, width/2 - 45, 100)

    elif state == "game":

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
                    if (boxx not in player_1_boxes and
                       boxx not in player_2_boxes):
                            player_1_boxes.append(boxx)
                            temp = True
                elif turn == "p1":
                    if (boxx not in player_2_boxes and
                       boxx not in player_1_boxes):
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
                 (LINE_DIS_1) - (LINE_DIS_1/3.2),
                 (LINE_DIS_2) - (LINE_DIS_2/2.4))

        fill(PLAYER_2_COLOUR[0], PLAYER_2_COLOUR[1], PLAYER_2_COLOUR[2])
        for dabba in player_2_boxes:
            rect(dabba[0] + (LINE_DIS_1/6.4), dabba[1] + (LINE_DIS_1/6.4),
                 (LINE_DIS_1) - (LINE_DIS_1/3.2),
                 (LINE_DIS_2) - (LINE_DIS_2/2.4))

        fill(178, 34, 34)
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

        strokeWeight(width/100)

        # Drawing Player Lines
        for write in p1_lines:
            stroke(PLAYER_1_COLOUR[0], PLAYER_1_COLOUR[1], PLAYER_1_COLOUR[2])
            line(write[0][0], write[0][1], write[1][0], write[1][1])

        for write in p2_lines:
            stroke(PLAYER_2_COLOUR[0], PLAYER_2_COLOUR[1], PLAYER_2_COLOUR[2])
            line(write[0][0], write[0][1], write[1][0], write[1][1])

        # Writing Who's Turn It Is
        fill(178, 34, 34)
        if turn == "p1":
            textSize((width + height)//25)
            text("Player 1", width/2 - width/9, height/15)
        elif turn == "p2":
            textSize((width + height)//25)
            text("Player 2", width/2 - width/9, height/15)

        # Telling the player if they are a noob
        if bad_line:
            textSize(30)
            text((turn.upper() + ", Please put a proper line"),
                 50, height - 50)

        if end_game(GRID_WID, GRID_LEN, player_1_boxes, player_2_boxes):
            background(238, 232, 170)
            p1_score = len(player_1_boxes)
            p2_score = len(player_2_boxes)

            if p1_score > p2_score:
                win = "Player 1"
            elif p1_score < p2_score:
                win = "Player 2"
            else:
                win = "Draw"

            fill(0)

            textSize(40)

            if win != "Draw":
                text((str(win) + " has won!"), 80, 50)
            else:
                text("It's a draw!", 100, 50)

            textSize(30)

            text("Score", 175, 150)

            textSize(25)
            text(("P1: " + str(p1_score)), 100, 200)
            text(("P2: " + str(p2_score)), 250, 200)

            textSize(20)

            text("Press any key to return to menu", 60, height - 50)

        if prompt:
            fill(255)
            stroke(0)
            strokeWeight(1)

            rect(100, 100, 200, 200)
            fill(0)
            textSize(15)
            text("""                 Are you sure you want
                 to return to restart?
                 Your game will
                 be lost""", 40, 130)
            text("Y = YES   N = NO", 120, 250)
        elif menu_prompt:
            fill(255)
            stroke(0)
            strokeWeight(1)

            rect(100, 100, 200, 200)
            fill(0)
            textSize(15)
            text("""                 Are you sure you want
                 to return to menu?
                 Your game will
                 be saved""", 40, 130)
            text("Y = YES   N = NO", 120, 250)

        noStroke()

        # Setting color of position cursor and drawing cursor
        if selection:
            fill(SELECTION_COLOUR[0], SELECTION_COLOUR[1], SELECTION_COLOUR[2])
        else:
            if turn == "p1":
                fill(CURSOR_COLOUR_P1[0],
                     CURSOR_COLOUR_P1[1],
                     CURSOR_COLOUR_P1[2])
            elif turn == "p2":
                fill(CURSOR_COLOUR_P2[0],
                     CURSOR_COLOUR_P2[1],
                     CURSOR_COLOUR_P2[2])
        ellipse(position[0], position[1], CURSOR_SIZE, CURSOR_SIZE)

        # Drawing Cursor
        fill(SELECTABLE_COLOUR[0], SELECTABLE_COLOUR[2], SELECTABLE_COLOUR[2])
        if selection:
            noStroke()
            ellipse(temp_line[0][0], temp_line[0][1], DOT_SIZE, DOT_SIZE)

            temp_dis = sqrt(((position[0] - temp_line[0][0]) ** 2) +
                            ((position[1] - temp_line[0][1]) ** 2))

            strokeWeight(1)

            if (temp_dis == LINE_DIS_1 or
               temp_dis == LINE_DIS_2):
                stroke(0, 250, 0)
            else:
                stroke(255, 0, 0)

            line(position[0], position[1], temp_line[0][0], temp_line[0][1])

            # print(temp_dis, LINE_DIS_1, LINE_DIS_2)


def end_game(wid, leng, p1_box, p2_box):
    total_boxes = (wid - 1) * (leng - 1)
    cur_boxes = len(p1_box) + len(p2_box)

    if total_boxes == cur_boxes:
        return True
    else:
        return False


def tests(lines, dots):
    for linee in lines:
        assert linee[0] in dots, "rouge line detected"
        assert linee[1] in dots, "illegal line has crossed the border"

    assert position in dots, "you're off the tracks"


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
    global state, select, colour_choice, select_prev
    global menu_prompt, prompt, colour_choice_1, colour_choice_2
    # print(keyCode)

    if state == "game":
        # Importing Global Variables
        global position, dots, pos_index, selection, win
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
        elif (keyCode == KEY_ENTER or keyCode == KEY_SPACE):

            if not selection:
                temp_line = [position]

                selection = True
            elif selection:

                temp_line += [position]

                # print(temp_line)

                distance = sqrt(((temp_line[0][0] - temp_line[1][0]) ** 2) +
                                ((temp_line[0][1] - temp_line[1][1]) ** 2))

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
        elif ((keyCode == KEY_R) or (keyCode == KEY_N) or
              (keyCode == KEY_Y) or (keyCode == KEY_M)):
            menu(keyCode)

        if isinstance(win, str):
            reset()
            state = "menu"

    elif state == "menu":
        global player_cul_choice, select_cul, colour_choice

        # print(select)

        if keyCode == KEY_M:
            if isinstance(select, str):
                select = select_prev

            for op in OPTIONS:
                if select in op:
                    select = op[0]

        if (keyCode == KEY_UP or keyCode == KEY_DOWN or
           keyCode == KEY_LEFT or keyCode == KEY_RIGHT):

            try:
                if keyCode == KEY_UP or keyCode == KEY_LEFT:
                    select -= 1
                elif keyCode == KEY_DOWN or keyCode == KEY_RIGHT:
                    select += 1
            except:
                select = select

            if isinstance(select, int):
                if select >= 5:
                    select = 1
                elif select < 1:
                    select = 4

        elif (keyCode == KEY_SPACE or keyCode == KEY_ENTER and
              select != "Options"):
            try:
                select = OPTIONS[select-1][1]
            except:
                select = select

        if keyCode == 49:
            player_cul_choice = 1
        elif keyCode == 50:
            player_cul_choice = 2

        if keyCode == KEY_UP or keyCode == KEY_RIGHT and select == "Options":
            select_cul += 1
        if keyCode == KEY_DOWN or keyCode == KEY_LEFT and select == "Options":
            select_cul -= 1

        if (keyCode == KEY_ENTER or keyCode == KEY_SPACE and
           select == "Options"):
            if choice == "P1":
                colour_choice_1 = select_cul
            elif choice == "P2":
                colour_choice_2 = select_cul

        if select_cul < 1:
            select_cul = 6
        elif select_cul > 6:
            select_cul = 1

        if isinstance(select, int):
            select_prev = select


def menu(key_given):
    global state, select
    global prompt, menu_prompt

    # print(prompt)

    if key_given == KEY_R:
        prompt = True
    elif key_given == KEY_M:
        menu_prompt = True

    if prompt:
        if prompt and key_given == KEY_Y:
            reset()
        elif prompt and key_given == KEY_N:
            prompt = False
    elif menu_prompt:
        if menu_prompt and key_given == KEY_Y:
            select = 1
            state = "menu"
            menu_prompt = False
        elif menu_prompt and key_given == KEY_N:
            menu_prompt = False

    # print("did it", prompt)

    return prompt


def instructions():
    inst = """
    How to play this game:
    - The objective of this game is to create lines to form boxes
    - The person with the most boxes at the end wins.

    CONTROLS
    - Use the arrow keys to move the cursor
    - Use enter/space to select a dot
          - When selecting a line, a thin line will be created.
          - If the line is green: the line is of a proper length
          - If the line is red: the line is too long
          - Lines must be 1 unit long
    - M to return to the menu
    - R to restart the game
    - Y to respond YES to prompts
    - N to respond NO to prompts
    """
    return inst


def info():
    information = """
    This game was created by:
    Sridhar Sairam for his ICS3U1 CPT.

    The final version of this game was made on:
        15 January 2019

    This game was made using Processing for Python.

    For further details, please contact Sridhar Sairam.
    """
    return information


def reset():

    global position, pos_index, dots, p1_lines, p2_lines, player_cul_choice
    global temp_line, player_1_boxes, player_2_boxes, lines
    global selection, bad_line, turn, select, prompt, win, select_cul
    global colour_choice, select_prev, choice, menu_prompt, player_cul_choice
    global colour_choice_1, colour_choice_2

    fill(0)
    stroke(0)
    strokeWeight(1)

    select_cul = 0

    colour_choice = 0
    select_prev = 0

    choice = "P1"

    player_cul_choice = 0

    colour_choice_1 = 1
    colour_choice_2 = 2

    position = []
    pos_index = 0
    dots = []
    lines = []
    p1_lines = []
    p2_lines = []
    temp_line = []

    player_1_boxes = []
    player_2_boxes = []

    win = 0

    player_cul_choice

    selection = False
    bad_line = False
    turn = "p1"

    prompt = False
    menu_prompt = False

    select = 1

    setup()
