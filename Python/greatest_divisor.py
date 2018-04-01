# Program that finds the greatest common divisor (GCD) for two user-supplied integers
import sys

def main():

    def greatest_cd(num1, num2):

        num1, num2 = int(num1), int(num2)

        while int(num2) != 0:
            num1, num2 = num2, num1%num2

        if int(num2) == 0:
            print()
            print("The GCD of " + str(user1) + " and " + str(user2) + " is: " + str(num1))
            print()
            print("Let's do it again! (Press <Enter> twice to exit)")
            print()

    user1 = str(input("Type in the first integer: "))
    user2 = str(input("Type in the second integer: "))

    while (user1 != "") or (user2 != ""):
        greatest_cd(user1, user2)
        user1 = str(input("Type in the first integer: "))
        user2 = str(input("Type in the second integer: "))


main()
