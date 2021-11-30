#Peep peep poop poop

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

def f(l, r, A):

    if l == r: return (A[l], A[l], A[l], A[l])
 
    mid = (l + r) // 2
     
    (Lmax, Lstart, Lend, Lsum) = f(l, mid, A)    
    (Rmax, Rstart, Rend, Rsum) = f(mid+1, r, A)

    Astart = max(Lstart, Lsum+Rstart, Lsum+Rsum)

    Aend = max(Rend, Rsum+Lend, Lsum+Rsum)

    Asum = Lsum+Rsum
    
    Amax = max(Astart, Aend, Asum, Lmax, Rmax, Lend+Rstart)

    return (Amax, Astart, Aend, Asum)

def test():
    testlist = [-6, 5] # [6, -5, 8, 2, -10, 2, 7, -1] = 11 [-2, 1, 3, 1, 11, -5, 1, -9] = 16 [-10, 2, -11, 5, 8, 2, -7, 2] = 15 [6, -5, 8, 2, -10, 2, 7, -1, -2, 1, 3, 1, 11, -5, 1, -9] = 23
    max = (f(0, len(testlist)-1, testlist))
    print(max[0])


test()
