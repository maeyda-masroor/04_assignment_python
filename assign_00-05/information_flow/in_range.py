
def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

def main():
    print(in_range(5, 1, 10))  # Example test case

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
