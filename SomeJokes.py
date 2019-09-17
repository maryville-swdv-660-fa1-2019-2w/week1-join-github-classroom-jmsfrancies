from graphics import *
from colorama import *


def Memes():
    win = GraphWin("Here Are Some Memes", 400, 400)
    win.getMouse()
    Slogan = Text(Point(
        200, 200), "Dave and Charles are urinating off of a bridge.\nCharles says that the water is cold.\nDave says the water is deep too!")
    Slogan.setTextColor("blue")
    Slogan.setSize(10)
    Slogan.draw(win)
    win.getMouse()
    Slogan.undraw()
    Slogan = Text(Point(
        200, 200), "What is six inches long, two inches wide,\nand women love to blow?\n Money!")
    Slogan.setTextColor("red")
    Slogan.setSize(10)
    Slogan.draw(win)
    win.getMouse()
    Slogan.undraw()


def main():
    init()
    print(Fore.RED)
    print(Back.GREEN)
    Question = int(input("Would You Like To See Some Memes Yes or No? (1/2)"))
    if Question == 1:
        Memes()
    else:
        Question = input("Press Any Key To Escape: ")


main()
