import random

NUM_SIDE = 6

def rolldice():
    #select random number from 1 till 6 for both total has different value than in main die1
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
