from graphics import *

def main():

# Define / open GraphWin, draw first square

    win = GraphWin("Dice",800,300)
    win.setCoords(0.0, 0.0, 16.0, 6.0)
    rect = Rectangle(Point(1.0,2.0), Point(3.0, 4.0))
    shift = 0.0

# Draw remaining squares

    for dice in range(5):
        new = rect.clone()
        new.draw(win)
        shift = shift + 3.0
        new.move(shift,0)

    rect.draw(win)

# Close out when clickedS    
    win.getMouse()
    win.close()

main()
