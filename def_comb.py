def comb(n,k):
    result=1
    for i in range(k):
        result*=n
        n-=1
    while k>0:
        result//=k
        k-=1 
    return result