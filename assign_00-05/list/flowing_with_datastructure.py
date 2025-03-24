def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

#python3 flowing_with_datastrucutre