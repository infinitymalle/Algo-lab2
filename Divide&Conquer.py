import random
import math
import cProfile

def CreateData():
    dataset = []

    for i in range(3*2**5):
        dataset.append(random.randrange(0, 101))    # choose number between 0 and 50 at random
        #dataset.append(i)                          # fills the dataset with already sorted data
        # Creates an almost sorted dataset, every tenth loop the input will be randomized
        #if i % 10 == 0: dataset.append(random.randrange(0, 101))
        #else: dataset.append(i)
    #print("test", dataset)
    print(dataset)
    return dataset


def divide(lst):
    half = len(lst) // 2
    # Base case, n == 3
    # Sorts the remaining 3 elements and returns sorted list
    if len(lst) == 3:
        if lst[0] > lst[1]:
            temp = lst[0]
            lst[0] = lst[1]
            lst[1] = temp
        if lst[0] > lst[2]:
            temp = lst[0]
            lst[0] = lst[2]
            lst[2] = temp
        if lst[1] > lst[2]:
            temp = lst[1]
            lst[1] = lst[2]
            lst[2] = temp
            
        return(lst)

    # Recursive Divide and Conquer
    else:
        Llst = divide(lst[0:half])
        Rlst = divide(lst[half:])
        
    # Compare the smallest value from 2 sorted lists 3 times,
    # Pop the smallest and put in new list for each loop which will then be returned
    finallst = []
    for i in range(3):
        if Rlst[0] < Llst[0]:
            finallst.append(Rlst[0])
            Rlst.pop(0)
        else:
            finallst.append(Llst[0])
            Llst.pop(0)

    return(finallst)

def test():
    data = CreateData()
    print(data)
    data = divide(data)
    print(data)

test()
