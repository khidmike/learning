from graphics import *

def main():
#

    class Button:

        def __init__(self, win, center, width, height, label):

            w,h = width/2.0, height/2.0
            x,y = center.getX(), center.getY()
            self.xmax, self.xmin = x+w, x-w
            self.ymax, self.ymin = y+h, y-h
            point1 = Point(self.xmin, self.ymin)
            point2 = Point(self.xmax, self.ymax)
            self.rect = Rectangle(point1, point2)
            self.rect.draw(win)
            self.label = Text(center, label)
            self.label.draw(win)




# Draw initial UI (text boxes, labels)
    window = GraphWin("First Bank of Boston", 600, 400)
    window.setCoords(0.0, 0.0, 30.0, 20.0)
    userButton = Button(window, Point(8.0, 13.0), 10, 2, "User ID")
    pinButton = Button(window, Point(6.0, 9.0), 6, 2, "PIN")
    login = Button(window, Point(24.0, 11.0), 8, 4, "LOGIN")


# Validate credentials
# If incorrect, display error
# If correct, display balances, draw logout / exit buttons
# If logout pressed, goes back to initial UI
# If exit pressed, closes window

    window.getMouse()
    window.close()

main()
