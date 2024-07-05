import random

def create(m, n):
    mat = []
    for _ in range(m):
        for _ in range(n):
            # mat.append(random.uniform(0.0, 1.0))
            mat.append(random.randint(1,5))
    return mat

def mat_mul(a,b,m,n,p):
    c = [0 for _ in range(m*p)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i * p + j] += a[i * n + k] * b[k * p + j]
    
    return c

m = 2
n = 3
p = 2

a = create(m, n)
b = create(n, p)
c = mat_mul(a, b, m, n, p)

import numpy as np
a1 = np.array(a).reshape(m, n)
b1 = np.array(b).reshape(n, p)
c1 = np.matmul(a1, b1).flatten()
print(np.allclose(c1, c))



