import numpy as np
"""SLICING"""
arr=np.array([45,89,13,45,85,13,89,56,79,16,54])
arr1=arr[3:6]
print(arr1)
r=arr1[0]=67
# print(arr1)
print(arr1)

"""THIS FUNCTION GIVES INDEX"""
# arr1=np.arange(6)
# print(arr1)

"""THIS FUNTION SORTS ARRAY"""
a=np.argsort(arr1)
print(a)
"""THIS FUNCTION GIVES MINIMUM NUMBER"""
b=np.argmin(arr)
print(b)
"""THIS FUNCTION GIVES MAXIMUM NUMBER"""
c=np.argmax(arr)
print(c)