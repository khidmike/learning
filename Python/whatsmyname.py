
from graphics import *

def main():

    # Define / open window
    win = GraphWin("Test", 700, 400)
    win.setCoords(0.0, 0.0, 42.0, 24.0)
    locationM = 2.0
    locationI = 14.0
    locationK = 19.0
    locationE = 30.0

    #Define functions for letters
    def drawM(window, location, color):
        window = window
        location = location
        m = Polygon(Point(location, location + 3.0), Point(location, location + 17.0), Point(location + 2.0, location + 17.0), Point(location + 5.0, location + 12.0), Point(location + 8.0, location + 17.0), Point(location + 10.0, location + 17.0), Point(location + 10.0, location + 3.0), Point(location + 7.0, location + 3.0), Point(location + 7.0, location + 12.0), Point(location + 5.0, location + 9.0), Point(location + 3.0, location + 12.0), Point(location + 3.0, location + 3.0)).draw(win)
        m.setFill(color)

    def drawI(window, location, color):
        window = window
        location = location
        i = Rectangle(Point(location, location - 9), Point(location + 3, location + 5)).draw(win)
        i.setFill(color)


    def drawK(window, location, color):
        window = window
        location = location
        k = Polygon(Point(location, location - 14), Point(location, location), Point(location + 3, location), Point(location + 3, location - 6), Point(location + 6, location), Point(location + 9, location), Point(location + 5.5, location - 7), Point(location + 9, location - 14), Point(location + 6, location - 14), Point(location + 3, location - 8), Point(location + 3, location - 14)).draw(win)
        k.setFill(color)

    def drawE(window, location, color):
        window = window
        location = location
        e = Polygon(Point(location, location - 25), Point(location, location - 11), Point(location + 8, location - 11), Point(location + 8, location - 13), Point(location + 2.5, location - 13), Point(location + 2.5, location - 17), Point(location + 5, location - 17), Point(location + 5, location - 19), Point(location + 2.5, location - 19), Point(location + 2.5, location - 23), Point(location + 8, location - 23), Point(location + 8, location - 25)).draw(win)
        e.setFill(color)


    #Draw name
    drawM(win, locationM, "blue")
    drawI(win, locationI, "green")
    drawK(win, locationK, "orange")
    drawE(win, locationE, "red3")




    win.getMouse()
    win.close()

main()
