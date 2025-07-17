import numpy as np
arr=np.array([[12,14,8,3,5],[13,9,26,29,11]])
arr1=np.array([[12,3,23,6,7],[11,15,2,5,14]])
print(arr,'\n')
"""THERE ARE TWO NEW THINGS FISRT 'AXIS' & SECOND 'KIND' """
# print(arr.sum(axis=0))
"""[25 23 34 32 16]"""
# print(arr.sum(axis=1))
"""[42 88]"""
"""TRANSPOSE METHOD"""
# print(np.dot(arr1,arr.transpose()))
"""CROSS METHOD"""
# print(np.cross(arr,arr1))"""phir se"""
"""REAL SORT FUNCTION"""
print(np.sort(arr,axis=1))