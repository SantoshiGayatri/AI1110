# Santoshi Gayatri Mavuru CS21BTECH11036
# Assiignment 4

import numpy as np
import random

N = 100000

def calc_Expectation(n):
  sum1 = 0
  for i in range(0, n):
    sum=np.zeros(n)
    sum[i]=0
    for j in range(0, N):
      x1= random.randint(1,6)
      x2= random.randint(1,6)
      if(x1!=x2):
        if(x1>x2):x=x1
        else:x=x2
        if(x==i):
          sum[i] += 1
    sum1+=((2*i*sum[i])/N)
  return float(sum1)

n=6
print( "E(X) = ",calc_Expectation(6))
print("Nearly equal to theoretical value 14/3")
