# Simple program to calculate the sum of user-supplied numbers

def main():

    nums = []
    print("Welcome to the Handy-Dandy Number Summer!")
    print()

    num = str(input("Enter your first number: "))
    while num != "":
        nums.append(num)
        num = str(input("Enter another number: "))

        def sumList(numbers):
            total = 0
            for i in nums:
                total = total + float(i)
            print()
            print("Your total sum is: " + str(total))

    sumList(nums)

main()
