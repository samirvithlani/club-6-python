import numpy as np

#create an array object....
arr = np.array([[1,2,3],[4,5,6]])

print(arr)
print(type(arr))
print(arr.ndim)

nested_list = [[[1, 2, 3,4], [5, 6, 7,4], [4, 10, 11, 12]],
               [[13, 14, 15,6], [6,17,  19, 20], [ 11,22, 23, 24]],[[13, 14, 15,8], [17,  19, 20,9], [ 22, 23, 24,66]]]
arr = np.array(nested_list)

print(arr.ndim)
print(arr.shape)
print(arr.dtype)
print(arr.size)