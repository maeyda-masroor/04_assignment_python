#write a program to convert farhenheit to celsious
def main():
    print("This program is about converting farhenhiet to celsious")
    farhenheit = input("Enter farhenheit")
    celcius = float((farhenheit-32)*5.0/9.0)
    print(str(celcius)+"C")

if __name__ == '__main__':
    main()