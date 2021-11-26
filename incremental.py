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


def incremental(list):
    element = list[len(list) -1]
    if len(list) == 3:
        return(sort(list))

    list = incremental(list[:-1])

    if (list[2] > element):
        if (list[1] > element):
            if (list[0] > element):
                list.insert(0, element)
            else:
                list.insert(1, element)
        else:
            list.insert(2, element)
    return(list[0:3])

def sort(list):





def divide(list):
    halv = len(list)/2
    
    if ((halv * 2)  == 3):
        return(sort(list))

    Llist = divide(list[0:halv])
    Rlist = divide(list[halv:-1])

    return(list[0:3])


#def incremental(list):          # väldigt inte klar
#    first3 = list[0:3]
#    list.insert(0, insertionsort(list[0:3]))    #0 till men inte med 3
#
#    for i in range(3, len(list)):
#        flag = 0
#        for j in range(2, 0, -1):
#            if list[i] > list[j]:
#                break
#            elif list[i] < list[j]: #yea fixa nåttt här bra här :)
#                
#
#                list.insert(j, list[i])
#                list.pop(i + 1)
#    return(list)


def insertionsort(list):                # gammla vanliga
    for i in range(len(list)):
        flag = 0
        j = i
        while(j > 0):
            j -= 1
            if (list[i] > list[j]):
                flag = 1
                break
        if (flag == 1):
            j += 1
        list.insert(j, list[i])
        list.pop(i + 1)
        
    return(list)

def test():
    data = CreateData()
    print(data)
    data = incremental(data)
    print(data)

test()

