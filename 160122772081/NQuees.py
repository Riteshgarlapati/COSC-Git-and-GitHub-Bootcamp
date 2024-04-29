n = 4
k = 0
x = [0]*n

def NQueens(k, n):
    if k == n:
        print(x)
        return
    for i in range(n):
        if place(k, i):
            x[k] = i
            NQueens(k+1, n)

def place(k, i):
    for j in range(k):
        if (x[j] == i) or abs(j-k) == abs(x[j]-i):
            return False
    return True

NQueens(k, n)