import numpy as np
import pandas as pd

data=np.array([[[32,31,35,60,7,35,37,32,60,7,30,32,38,60,8,48,41,46,60,9]]]).reshape(4,5)
df3=pd.DataFrame(data,index=["Aditya","Suryansh","Shivansh","Saksham"],columns=["|FOUNDATION OF DS|","|OPERATING SYSTEM|","|'C' PROGRAMING|","|TOTAL MARKS|","|CGPA|"])
# print(df3)

## SLICING

# print(df3[4::-1])

##
# print(df3.iloc[0:5:2,0:5:2])
"""first the slicing is going on indexes then,columns"""

##UPDATION
a=df3.loc["FOUNDATION OF DS","Shivansh"]=40
print(df3)
