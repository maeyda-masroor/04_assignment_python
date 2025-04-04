def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total_so_far: int = 0
    index: int = 0

    while (index < len(numbers)):
         total_so_far+=numbers[index]
         index+=1

    return total_so_far


def main():
    print("Add many number")
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers) 


if __name__ == '__main__':
     main()

#python3 add_many_number.py