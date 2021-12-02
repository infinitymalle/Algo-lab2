import random
import math
import cProfile

def CreateData():
    dataset = []

    for i in range(10):
        dataset.append(random.randrange(0, 101))    # choose number between 0 and 50 at random
        #dataset.append(i)                          # fills the dataset with already sorted data
        # Creates an almost sorted dataset, every tenth loop the input will be randomized
        #if i % 10 == 0: dataset.append(random.randrange(0, 101))
        #else: dataset.append(i)
    #print("test", dataset)
    return dataset


def incremental(lst):
    if len(lst) == 3:           #basfall -->vanlig bubbelsort
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
    
    element = lst[len(lst) -1]
    lst = incremental(lst[:-1])
    if lst[2] > element:                 #enkel jämförelse, placerar elementen på rätt plats
        if lst[1] > element:
            if lst[0] > element:
                lst.insert(0, element)
            else:
                lst.insert(1, element)
        else:
            lst.insert(2, element)

    return lst[0:3] #returnerar endast de tre första eftersom det fjärde är större


def test():
    data = CreateData()
    print(data)
    data = incremental(data)
    print(data)

test()

