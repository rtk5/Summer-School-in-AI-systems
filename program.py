import json
import sys
import random
import math

inp = json.loads(sys.stdin.read())
def create(inp):
    matrix = []
    for item in inp:
        item['swimmingPool'] = 1.0 if item['swimmingPool'] else 0.0
        row = [item['propertyAge'], item['balconies'], item['swimmingPool'], item['propertySize'], item['furnishingStatus'], item['rent']]
        matrix.append(row)
    return matrix

def create_rand_mat(m, n):
    return [[random.uniform(0.0, 1.0) for _ in range(n)] for _ in range(m)]

def mat_mul(a, b):
    if isinstance(a[0], list):
        row1 = len(a)
        col1 = len(a[0])
    else:
        a = [a]
        row1 = 1
        col1 = len(a[0])

    row2 = len(b)
    col2 = len(b[0])
    
    if col1 != row2:
        raise ValueError("Matrices cannot be multiplied.")
    
    c = [[0 for _ in range(col2)] for _ in range(row1)]
    
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                c[i][j] += a[i][k] * b[k][j]
    
    return c

matrix = create(inp)
# sample = matrix[0][0:5]
# print(sample)
sample=[]
for i in range(len(matrix)):
    sample.append(matrix[i][0:5])     #[1][5]
# print(sample)     # [500][5]

wts = create_rand_mat(5, 1)     # [5][1]

def model(wts, sample):
    a = mat_mul(sample, wts)
    return [max(a[i][0], 0) for i in range(len(sample))]

# print("output:", model(wts, sample))

rents=[]
for i in range(len(matrix)):
    rents.append(matrix[i][5]) 

def error(pred,rents):
    diff=0
    for i in range(len(rents)):
        diff+=(pred[i]-rents[i])*(pred[i]-rents[i])
    result = math.sqrt(diff/500)
    return result   

print("Error =",error(model(wts, sample),rents))

def step(x):
    if x>0:
        return 1
    else:
        return 0
 
def gradient(matrix, wts):
    n = len(matrix)
    sample = [row[:5] for row in matrix]
    rents = [row[5] for row in matrix]
    preds = model(wts, sample)
    err = error(preds, rents)
    
    gradients = [0] * len(wts)
    for j in range(len(wts)):
        temp = sum((preds[i] - rents[i]) * sample[i][j] for i in range(n))
        gradients[j] = (1 / n) * (1 / err) * temp
    
    return gradients

grad = gradient(matrix,wts)
print("The gradient is",grad)

def gradient_descent(matrix, wts):
    lr = 0.01
    sample = [row[:5] for row in matrix]
    rents = [row[5] for row in matrix]
    for i in range(100):
        grad = gradient(matrix, wts)
        for j in range(len(wts)):
            wts[j][0] -= lr * grad[j]
        preds = model(wts, sample)
        err = error(preds, rents)
        print(f"Iteration {i+1}, Error: {err}")
    return 0
    
print("Gradient descent",gradient_descent(matrix,wts))
