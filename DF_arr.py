import numpy as np
import pandas as pd

"""this is an empty data frame"""

# df=pd.DataFrame()
# print(df,"\n")

"""this is a static data frame"""

# df1=pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(df1)

"""now we do naming in index and column"""

d=np.array([[1,2,3,4,5,6,7,8,9,10,11,12,20,20,20,20,20,20]]).reshape(3,6)
df2=pd.DataFrame(d,index=["ayu","ayush","out_of"],columns=["marks_1","marks_2","marks_3","marks_4","marks_5","marks_6"])
print(d.size)

"""question regarding to this topic"""
# data=np.array([[32,31,45,35,37,42,30,32,38,48,41,46]]).reshape(4,3)
# df3=pd.DataFrame(data,index=["Aditya","Suryansh","Shivansh","Saksham"],columns=["FOUNDATION OF DS","OPERATING SYSTEM","'C' PROGRAMING"])
# print(df3)

## TO PRINT THE SINGLE COLUMN OF A ROW
# print("THIS IS MARKS OF 'OS':",df3.loc["Saksham","OPERATING SYSTEM"])

## TO PRINT SINGLE COLUMN OF 'N' ROWS
# print(df3.loc[["Saksham","Aditya"],["OPERATING SYSTEM"]])
# """IT USES 3 SQUARE BRACES """