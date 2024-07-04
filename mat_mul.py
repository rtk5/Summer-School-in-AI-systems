import random
import time
import matplotlib.pyplot as plt
import numpy as np

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
        raise ValueError("Matrices cannot be multiplied.")
    
    c = [[0 for _ in range(col2)] for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                c[i][j] += a[i][k] * b[k][j]
    
    return c

def benchmark(start, end, step):
    times = []
    dimensions = []
    flops = []
    
    for i in range(start, end, step):
        a = create(i+1, i+1)
        b = create(i+1,i+1)

        start_time = time.time()
        c = mat_mul(a, b)
        # c=np.matmul(a,b)
        
        end_time = time.time()

        time_taken = end_time - start_time
        times.append(time_taken)
        dimensions.append(i)
        
        total=end_time - start_time
        flop = 2 * i**3 / total 
        flops.append(flop)

    return dimensions, times, flops

start = 0   
end = 200   
step = 50   
dimensions, times, flops = benchmark(start, end+1, step)

plt.figure(figsize=(10, 6))
plt.plot(dimensions, times, marker='o', linestyle='-', color='b', label='mat_mul')
plt.title('Time vs Matrix Dimensions')
plt.xlabel('Matrix Dimension (size)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(dimensions, flops, marker='o', linestyle='-', color='b', label='mat_mul')
plt.title('Flops vs Matrix Dimensions')
plt.xlabel('Matrix Dimension (size)')
plt.ylabel('Flops')
plt.grid(True)
plt.tight_layout()
plt.show()
