# Simple program using a Caesar Cipher to encode / decode text strings
import sys

def main():

    print("Welcome to the Caesar Cipher Encoder / Decoder")
    print()

    coding = str(input("What would you like to do? Type 'e' to encode / 'd' to decode: "))

    if (coding != "e") and (coding != "d"):
        print("I'm sorry... I don't understand what you want me to do")
        sys.exit()

    key = int(input("What is the key you would like to use? Type a number 1-25: "))
    text = list(str(input("What is the text you would like to encode: ")))
    result = []

    if coding == "e":
        for char in text:
            result.append(chr(ord(char) + key))

    elif coding == "d":
        for char in text:
            result.append(chr(ord(char) - key))

    print("Your result is: ")
    print()
    print("".join(result))




main()
