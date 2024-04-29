def LCS(x,y):
  m = len(x)
  n = len(y)
  L = [[0 for x in range(n+1)] for x in range(m+1)]
  for i in range(m+1):
    for j in range(n+1):
      if i==0 or j==0:
        L[i][j] = 0
      elif x[i-1] == y[j-1]:
        L[i][j] = L[i-1][j-1]+1
      else:
        L[i][j] = max(L[i-1][j],L[i][j-1])
  return L[m][n]

x = ['a','b','c','d','e','f','g']
y = ['x','z','a','c','k','d','f']
print(LCS(x,y))