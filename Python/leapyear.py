# A program to test whether a user-given four-digit year is a leap leap_year

def main():

    def leap_year(year):
    # test whether it is four-digit
    # if not, prompt again
        while len(str(year)) != 4:
            print()
            year = int(input("Sorry, your year must be four-digits long. Enter again: "))

        year = int(year)
    # otherwise, test for leap-year
        if len(str(year)) == 4:
            if year%4 != 0:
                print(str(year) + " is not a leap year!")
            elif (year%100 == 0) and (year%400 != 0):
                print(str(year) + " is not a leap year!")
            elif (year%400 == 0) or (year%4 == 0):
                print(str(year) + " is a leap year!")


    response = str(input("Welcome to the Leap Year tester! Please enter a four-digit year: "))

    while response != "":
        print()
        leap_year(response)
        print()
        response = str(input("Enter another year: "))

main()
