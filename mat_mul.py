import random
import timeit
import matplotlib.pyplot as plt

def create(m, n):
    mat = []
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(random.uniform(0.0, 1.0))
        mat.append(row)
    return mat

def mat_mul(a, b):
    row1 = len(a)
    row2 = len(b)
    col1 = len(a[0])
    col2 = len(b[0])
    
    if col1 != row2:
        raise ValueError("WRONG INPUT!!!!!!!!!!")
    c = [[0 for _ in range(col2)] for _ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                c[i][j] += a[i][k] * b[k][j]
    return c

def benchmark(n):
    times = []
    dimensions = []
    for i in range(n):
        a = create(i + 1, i + 1)
        b = create(i + 1, i + 1)

        start_time = timeit.default_timer()
        c = mat_mul(a, b)
        end_time = timeit.default_timer()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        dimensions.append(i + 1)

    return dimensions, times

n = 10  
dimensions, times = benchmark(n)

plt.figure(figsize=(10, 6))
plt.plot(dimensions, times, marker='o', linestyle='-', color='b', label='mat_mul')
plt.title('Time vs Matrix Dimensions')
plt.xlabel('Matrix Dimension (size)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
