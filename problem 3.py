# HW 1 Problem 3
def sum_iter(n):
    prod=0
    for i in range(1,n+1):
        prod+=i
    return prod

print(sum_iter(100))

def sum_rec(n):
    if n==1:
        return 1
    else:
        return n+sum_rec(n-1)

print (sum_rec(100))
