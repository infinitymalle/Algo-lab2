#peep peep poop poop

import random
import math
import cProfile

def CreateData():
    dataset = []

    for i in range(1000000):
        dataset.append(random.randrange(0, 101))    # choose number between 0 and 50 at random
        #dataset.append(i)                          # fills the dataset with already sorted data
        # Creates an almost sorted dataset, every tenth loop the input will be randomized
        #if i % 10 == 0: dataset.append(random.randrange(0, 101))
        #else: dataset.append(i)
    #print("test", dataset)
    return dataset


def divide(list):

    halv = len(list)/2
    
    if ((halv * 2)  == 3):
        return(sort(list))
    else:
        Llist = divide(list[0:halv])
        Rlist = divide(list[halv:-1])

    return(list[0:3])

def sort(list):
    return(list)