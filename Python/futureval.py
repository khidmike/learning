# Program to calculate compound interest
import datetime

def main():
    print("This program will calculate compound interest for a sum of money over a given number of years")
    year = datetime.date.today().year
    principal = eval(input("Type in the principal (starting) amount: "))
    apr = eval(input("Type in your interest rate in decimal form (e.g. 6% --> .06)"))
    years = eval(input("Type in how many years' interest you want to calculate: "))

    for i in range(years):
        principal = (principal * (1+apr))
        year = year + 1
        print("The value in " + str(year) + " will be: " + str(principal))

main()
