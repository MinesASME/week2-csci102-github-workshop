#Ryan Wagner
#CSCI 102
#Section B
#Week 12 - Github workshop 2

def fib():
    fibs = [1, 2]

    for i in range(2,100):
        fibs.append(fibs[i-1] + fibs[i-2])
    #print(len(fibs))
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
