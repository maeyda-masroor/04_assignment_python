
def main():
    integer_to_be_divided = input("Enter integer to be divided")
    integer_to_divide = input("Enrter an integer to divide")
    quotient = integer_to_be_divided // integer_to_divide
    reminader = integer_to_be_divided % integer_to_divide
    print("The result of this division is "+str(quotient)+"with a remainder of"+str(reminader))

if __name__ == '__main__':
    main()