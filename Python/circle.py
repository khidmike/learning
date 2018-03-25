from graphics import *

def main():

    radius = float(input("Enter a radius for your circle: "))
    area = (3.14 * (2 * radius))
    print("The area of your circle is: " + str(area))

    win = GraphWin("Circle", 200, 200)
    circ = Circle(Point(100,100), radius).draw(win)

    win.getMouse()
    win.close

main()
