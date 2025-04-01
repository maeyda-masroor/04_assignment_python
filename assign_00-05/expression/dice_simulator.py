import random

NUM_SIDE = 6

def rolldice():
    die1 = random.randint(1,NUM_SIDE)
    die2 = random.randint(1,NUM_SIDE)
    total = die1 + die2
    print("Total die"+str(total))

    
def main():
    die1 = 10
    print("Die1 starts as"+str(die1))
    rolldice()
    rolldice()
    rolldice()
    print("die in main as"+str(die1))

if __name__ == '__main__':
    main()
