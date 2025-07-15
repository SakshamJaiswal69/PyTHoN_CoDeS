import numpy as np
f1=np.array([[45,79,13,79],[79,0,58,64],[73,12,16,45],[85,32,56,13]])
# print(f1.size)
"""count elements"""
# print(f1.argmax(axis=1))
"""give index of highest values"""
# print(f1.argmin(axis=1))
"""give index of lowest values"""
# print(f1.ravel())
"""make any dimension to 1-D array"""
# print(f1.argsort())
"""give index to change value place """
# a=np.sort(f1)
"""change value place and print it """
# print(np.sort(f1))
# print("\n",a)
# print(np.all(f1))
"""checks all values and tell T/F by the presence of zero  """
print(np.any(f1))
"""it also checks that but it is like 'OR' func."""