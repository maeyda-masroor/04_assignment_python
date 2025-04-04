def main():
    numbers = [1, 2, 3, 4]  # Creates a list of numbers

    i  = 1 
    while (i < len(numbers)):
        elem_at_index = numbers[i]
        numbers[i] = elem_at_index * 2
        i+=1
    
    print(numbers)  # This should print the doubled list


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
