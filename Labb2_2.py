import random
import math
import cProfile

def f(Left, Right, A):

    if Left == Right: return (A[Left], A[Left], A[Left], A[Left])
 
    mid = (Left + Right) // 2
     
    # Lmax = biggest possible subarray, Lstart = must include leftmost element, Lend = must include rightmost element, Lsum = the sum of all elements
    (Lmax, Lstart, Lend, Lsum) = f(Left, mid, A)    
    # Rmax = biggest possible subarray, Rstart = must include leftmost element, Rend = must include rightmost element, Rsum = the sum of all elements
    (Rmax, Rstart, Rend, Rsum) = f(mid+1, Right, A)

    # The leftmost element must be included when combining Left and Right
    Astart = max(Lstart, Lsum+Rstart, Lsum+Rsum)

    # The rightmost element must be included when combining Left and Right
    Aend = max(Rend, Rsum+Lend, Lsum+Rsum)

    # The sum of Left and Right
    Asum = Lsum+Rsum
    
    # The maximum sum of a subarray created when combining Left and Right. 
    Amax = max(Astart, Aend, Asum, Lmax, Rmax, Lend+Rstart)

    return (Amax, Astart, Aend, Asum)

def test():
    testlist = [-6, 5] # [6, -5, 8, 2, -10, 2, 7, -1] = 11 [-2, 1, 3, 1, 11, -5, 1, -9] = 16 [-10, 2, -11, 5, 8, 2, -7, 2] = 15 [6, -5, 8, 2, -10, 2, 7, -1, -2, 1, 3, 1, 11, -5, 1, -9] = 23
    max = (f(0, len(testlist)-1, testlist))
    print(max[0])


test()
