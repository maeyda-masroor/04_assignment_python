#Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def main():
    print("In this program, we are going to discuss our favorite animal.")
    favorite_animal = input("What's your favorite animal? ")
    print(f"My favorite animal is also {favorite_animal}!")

if __name__ == '__main__':
    main()

#run with python3 agreement_bot.py
