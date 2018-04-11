# The assignment is to write your first name(or a nickname or initials - at least 3 different characters). However  - you need to use the python graphics library discussed in the textbook (this library has been provided to you in Eclipse on the VMWare image).  Program a main() function which sets up and scales your window. Then write code to create a function for each 'character' in your name - the function will draw the character any using graphics objects(point, line, circle, rectangle, etc..)to your window. Each function will need to accept the following parameters:
#
# Window to draw the character to
# Location to draw the character on the window(i.e. Point object with a location on the window)
# Optional color to draw your character
# Sample psuedo code  to draw the characters 'Steve' to a graphics window:
#
# Create graphics window
# Scale Graphics Window
# Call function DrawUppcaseS(Window,Location1,Red)
# Call function DrawLowerCaseT(Window,Location2,Red)
# Call function DrawLowerCaseE(Window,Location3,Red)
# Call function DrawLowerCaseV(Window,Location4,Red)
# Call function DrawLowerCaseE(Window,Location5,Red)
# Prompt for user input so Graphics Window remains visible
# Note: The location variable point values must be set in the main() function. You can set numeric values or get the current location from a mouse click using the graphics library, but either way these values must be set in the main() function.
# You must create at least 3 different characters - you can abbreviate your name if desired. You will not be graded on the creative style of the appearance of your characters, however your characters need to be "simply recognizable". We are not looking to create a new font just yet !

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
