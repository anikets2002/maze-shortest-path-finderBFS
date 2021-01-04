import queue
import curses
import time


def createMaze(stdscr):
    stdscr.addch(9,9 ,"x")                                                                                              #FOOD Co-ordinates
    sh, sw = stdscr.getmaxyx()

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)                                                         #Creating text boxes
    text_box_1 = curses.newwin(4, 25, 5, 30 )
    text_box_1.attron(1)
    text_box_1.border()
    text_box_1.bkgd(curses.color_pair(2))
    text_1 = "DEFIANZ PROJECT"

    text_box_1.addstr(2,4 , text_1)

    text_box_1.attroff(1)
    text_box_1.refresh()

    text_box_2 = curses.newwin(4, 25, 12, 30 )
    text_box_2.attron(1)
    text_box_2.border()
    text_box_2.bkgd(curses.color_pair(2))
    text_2 = "MADE BY:- ANIKET SINGH"

    text_box_2.addstr(2,2, text_2)

    text_box_2.attroff(2)
    text_box_2.refresh()                                                                                                #Creation Complete

    """MAZE CREATION BEGINS"""
    box1 = stdscr.subwin(20,20, 0, 0)                                                                                   #Maze Creation
    box2 = stdscr.subwin(16,16, 2, 2)
    box3 = stdscr.subwin(12,12, 4, 4)
    box4 = stdscr.subwin(8,8, 6, 6)
    box5 = stdscr.subwin(4,4, 8, 8)

    box1.border(",",",",",",",",",",",",",",",")
    box2.border(",",",",",",",",",",",",",",",")
    box3.border(",",",",",",",",",",",",",",",")
    box4.border(",",",",",",",",",",",",",",",")
    box5.border(",",",",",",",",",",",",",",",")

    box2.hline(0, 15, " ",1)
    box2.hline(0, 2, " ",1)
    box2.hline(15, 11, " ",1)

    box3.hline(0, 3, " ",1)
    box3.hline(11, 5, " ",1)

    box4.hline(0, 3, " ", 1)
    box4.hline(7, 4, " ",1)

    box5.hline(0,1," ",1)

    box2.vline(1,0," ",1)
    box2.vline(7, 0, " ", 1)
    box2.vline(13,15, " ",1)

    box3.vline(6, 0, " ",1)
    box3.vline(9,10, " ",1)

    box4.vline(7, 3, " ",1)
    """MAZE CREATION ENDS"""

    stdscr.refresh()


def move_mouse(stdscr, moves):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_RED)
    stdscr.attron(curses.color_pair(1))

    posX = 1
    posY = 2

    stdscr.addstr(posY,posX, " ")
    stdscr.refresh()
    for move in moves:

        if move == "L":
            posX -= 1

        elif move == "R":
            posX += 1

        elif move == "U":
            posY -= 1

        elif move == "D":
            posY += 1

        time.sleep(0.5)
        stdscr.addstr(posY,posX," ")

        stdscr.refresh()

    stdscr.attroff(curses.color_pair(1))

def valid(stdscr, moves):
    sh, sw = stdscr.getmaxyx()
    createMaze(stdscr)
    i = 1
    j = 2
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 < i < 20 and 0 < j < 20):
            return False
        elif stdscr.inch(j, i) == ord(","):
            return False

    return True

def findEnd(stdscr, moves):

    sh, sw = stdscr.getmaxyx()
    createMaze(stdscr)
    i = 1
    j = 2
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
    if stdscr.inch(j,i) == ord("x"):
        curses.beep()
        print("Found: " + moves)
        print(moves)
        stdscr.addstr(27,1, "Shortest Sequence:")
        stdscr.addstr(29,1, "CONGRATULATIONS!! MOUSE FOUND THE FOOD")
        move_mouse(stdscr, moves)
        stdscr.refresh()
        return True

    return False

# MAIN ALGORITHM
def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    current_list = queue.Queue()
    current_list.put("")
    add = ""
    createMaze(stdscr)

    while not findEnd(stdscr, add):
        add = current_list.get()

        for j in ["L", "R", "U", "D"]:
            current_item = add + j
            if valid(stdscr, current_item):
                current_list.put(current_item)
                stdscr.addstr(27,2, "Current Sequence:")
                stdscr.addstr(27, 20, current_item)
                stdscr.refresh()

    stdscr.getch()

curses.wrapper(main)