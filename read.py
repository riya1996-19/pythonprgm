# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:20:05 2021

@author: riya2
"""
Created on Sat Aug 28 15:58:59 2021
@author: 
#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
    
df = pandas.read_csv('D:/skillfiles/files/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('D:/skillfiles/files/User_Data.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('D:/skillfiles/files/User_Data.xlsx')

df1 = pandas.read_excel('D:/skillfiles/files/User_Data.xlsx')

































































































































































































































































































































































































































































































































































































































































































































































































































































































# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)