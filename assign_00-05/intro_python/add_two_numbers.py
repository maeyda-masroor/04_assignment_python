#Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
def main():
    print("In this program we add two numbers...")
    #enter 1st number ... and convert it into int
    num1 = input("Enter first number")
    num1 = int(num1)
    #enter 2nd number ... and convert it into int
    num2 = input("Enter second number")
    num2 = int(num2)
    total = num1 + num2
    print("The total is"+str(total)+".")

if __name__ == '__main__':
    main()

