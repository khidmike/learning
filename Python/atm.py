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
            self.rect.draw(win).setFill("red")
            self.label = Text(center, label)
            self.label.draw(win)




# Draw initial UI (text boxes, labels)
    window = GraphWin("First Bank of Boston", 600, 400)
    window.setCoords(0.0, 0.0, 30.0, 20.0)
    Text(Point(5.0, 18.0), "Enter username: ").draw(window)
    Text(Point(4.0, 16.0), "Enter PIN: ").draw(window)
    username = Entry(Point(16.0, 18.0), 20).draw(window)
    pin = Entry(Point(16.0, 16.0), 20).draw(window)
    login = Button(window, Point(26.0, 12.0), 6, 3, "LOGIN")

    chbal = Text(Point(5.0, 7.0), "Checking Balance: ").draw(window)
    sabal = Text(Point(4.75, 4.0), "Savings Balance: ").draw(window)



    # userlist = open("C:/Users/Misha/Desktop/userlist.txt", "r")
    # first = userlist.readline()
    # username, pin, chbal, sabal = first.split("\t")

    # check = Text(Point(15.0, 7.0), chbal).draw(window)

    # for line in userlist:
    #     test = Text(username, chbal, sabal)
    #     test.draw(window)


# Validate credentials
    #read through file until match found for name
    # def validate(username, pin):
    #
    #     userlist = open("C:/Users/Misha/Desktop/userlist.txt", "r")
    #
    #     for line in userlist:


# If incorrect, display error
#   if (incorrect info):
#       print("Incorrect UserID or PIN")

# If correct, display balances, draw logout / exit buttons
# If logout pressed, goes back to initial UI
# If exit pressed, closes window

    window.getMouse()
    window.close()

main()
