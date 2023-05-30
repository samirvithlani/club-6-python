import numpy as np
a = np.array([[1,4,3],[4,5,6],[3,2,1]])
# print(a)
# print(a.max())
# print(a.min())

# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))


print(np.sort(a))
print(np.sort(a,axis=0,kind='mergesort'))
print(np.sort(a,axis=1))


print(np.sqrt(a))


# print(a.sin())
# print(a.cos())
# print(a.tan())
# print(a.sqrt())
# print(a.exp())
