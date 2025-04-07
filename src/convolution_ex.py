import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

input_array = np.full((7,7), 0)
input_array[0:2, 0:7] = 1
input_array[2:3, 0:6] = 1
input_array[3:4, 0:4] = 1
input_array[4:5, 0:2] = 1

kernel_array = np.full((3,3), -1)
kernel_array[1,1] = 8

result_array = np.full((5,5), -1)

def convolve(data, kernel, r, c):
    field = data[r-1:r+2, c-1:c+2]
    return np.sum(field*kernel)

for i in range(5):
    for j in range(5):
        result_array[i,j] = convolve(input_array, kernel_array, i+1, j+1)

print(convolve(input_array, kernel_array, 2, 5))
print(input_array)
print(kernel_array)
print(result_array)


