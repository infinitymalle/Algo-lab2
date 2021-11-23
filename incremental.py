#peep peep poop poop

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

def incremental(list):      #fortfarande insertionsort
    for i in range(len(list)):
        if (i <= 2):
            continue
        for j in range(2, 0, -1):
            if i < j:
                break
            list.insert(j, list[i])
            list.pop(i + 1)

        
        
    return(list)

def test():
    data = CreateData()
    print(data)
    data = incremental(data)
    print(data)

test()

