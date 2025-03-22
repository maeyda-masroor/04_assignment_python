## Problem Statement


def main():
    input_1 = input("Enter length for side 1 ")
    side_1 = float(input_1)
    input_2 = input("Enter length for side 2")
    side_2 = float(input_2)
    input_3 = input("Enter length for side 3")
    side_3 = float(input_3)
    perimter = float(side_1 + side_2 + side_3) 
    print("The perimeter is " + str(perimter))
if __name__ == '__main__':
    main()
