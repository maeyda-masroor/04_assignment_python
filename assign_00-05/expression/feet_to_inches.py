INCHES_IN_FOOT = 12

def main():
    feet = input("enter feet")
    inches = float(feet * INCHES_IN_FOOT)
    print("This is " + str(inches) + "inches!")
if __name__ == '__main__':
    main()
