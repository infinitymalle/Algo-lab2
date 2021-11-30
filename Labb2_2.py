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
