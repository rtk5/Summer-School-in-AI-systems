import random

def create(m, n):
    mat = []
    for _ in range(m):
        for _ in range(n):
            # mat.append(random.uniform(0.0, 1.0))
            mat.append(random.randint(1,5))
    return mat

def mat_mul(a,b,m,n,p,step):
    c = [0 for _ in range(m*p)]
    for batch in range(0,m,step):
        for i in range(batch, min(batch + step, m)):
            for j in range(p):
                for k in range(n):
                    c[i * p + j] += a[i * n + k] * b[k * p + j]
        print(c)
    
m = 4
n = 3
p = 4

a = create(m, n)
b = create(n, p)
c = mat_mul(a, b, m, n, p,2)

print("From numpy")
# print(c)

import numpy as np
a1 = np.array(a).reshape(m, n)
b1 = np.array(b).reshape(n, p)
c1 = np.matmul(a1, b1).flatten()
print(c1)



