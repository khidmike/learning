from graphics import *

def main():

# Define / open GraphWin, draw first square

    win = GraphWin("Dice",800,300)
    win.setCoords(0.0, 0.0, 16.0, 6.0)
    rect = Rectangle(Point(1.0,2.0), Point(3.0, 4.0))
    rect.draw(win)
    shift = 0.0

# Draw remaining squares

    for dice in range(5):
        new = rect.clone()
        new.draw(win)
        shift = shift + 3.0
        new.move(shift,0)

# Draw markings on dice

    one = Point(2.0, 3.0).draw(win)
    two1, two2 = Point(4.5, 3.5).draw(win), Point(5.5, 2.5).draw(win)
    three1, three2, three3 = Point(7.5, 3.5).draw(win), Point(8.0, 3.0).draw(win), Point(8.5, 2.5).draw(win)
    four1, four2, four3, four4 = Point(10.5, 3.5).draw(win), Point(10.5, 2.5).draw(win), Point(11.5, 3.5).draw(win), Point(11.5, 2.5).draw(win)
    five1, five2, five3, five4, five5 = Point(13.5, 3.5).draw(win), Point(14.5, 3.5).draw(win), Point(14.0, 3.0).draw(win), Point(13.5, 2.5).draw(win), Point(14.5, 2.5).draw(win)

# Close out when clickedS
    win.getMouse()
    win.close()

main()
