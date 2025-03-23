import math
def main():
    print("PYTHAGOREAN THEOREM")
    AB_length = input("Enter length of AB")
    AC_length = input("Enter length of AC")
    BC_length = math.sqrt(AB_length ** 2 + AC_length ** 2)
    print("The length of BC is"+str(BC_length))   
    
if __name__ == '__main__':
    main()