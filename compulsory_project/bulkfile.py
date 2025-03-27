import os
def main():
    i = 0
    path = "/Users/maeydahmasroor/Desktop/04_assignment/test/"
    for filename in os.listdir(path):
        mydest = "img"+str(i)+"jpg"
        my_source = path + filename
        mydest = path + mydest
        os.rename(my_source,my_source)
        i+=1

if __name__ == '__main__':
    main()
