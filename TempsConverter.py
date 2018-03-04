def main():
    print("This program converts Fahrenheit temperatures to Celsius")
    fahr = eval(input("Please enter a temperature in degrees Fahrenheit: "))
    cels = ((fahr-32)*(5/9))
    print("If the temperature in F is "+ str(fahr) + "then the temperature in Celsius is: " + str(cels))

main()
