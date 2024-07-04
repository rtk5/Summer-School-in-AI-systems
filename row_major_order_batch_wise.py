import random

def create(m, n):
    mat = []
    for _ in range(m):
        for _ in range(n):
            # mat.append(random.uniform(0.0, 1.0))
            mat.append(random.randint(1,5))
    return mat

def mat_mul(a,b,m,n,p,m_step,n_step):
    c = [0 for _ in range(m*p)]
    for batch in range(0,m,m_step):
        for batch2 in range(0,n,n_step):
            for i in range(batch, min(batch + m_step, m)):
                for j in range(p):
                    for k in range(batch2,min(batch2 + n_step, n)):
                        c[i * p + j] += a[i * n + k] * b[k * p + j]
    return c
    
m = 2
n = 3
p = 4
m_step = 5
n_step = 2

a = create(m, n)
b = create(n, p)
c = mat_mul(a, b, m, n, p, m_step, n_step)

print("From numpy")
# print(c)

import numpy as np
a1 = np.array(a).reshape(m, n)
b1 = np.array(b).reshape(n, p)
c1 = np.matmul(a1, b1).flatten()
assert np.allclose(c1, c)
print(np.allclose(c1, c))



