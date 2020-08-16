import numpy as np
import pandas as pd
from PythonCollections.MyList import MyList
import sys

# To disply site-packages location. Put user defined modules in site-packages
# print(sys.path)

a = np.array([0,1,2,3,4,5]) 
b = np.array(["Country","DummyValue1","DummyValue2"])
c = np.array([
    ["IND","One",100],
    ["USA","Two",200],
    ["GER","Three",300],
    ["AUS","Four",400],
    ["FRA","Five",500],
    ["UAE","Six",600]
])
df = pd.DataFrame(index=a,data=c,columns=b)
# print(df)
# To Print first 5 entries
# print(df.head())
# print(df.count())
# To Display full Column with index, df['ColumnName']
# print(df['Country'])
# To Display full multiple Columns with index, df['ColumnName']
# print(df[['Country','DummyValue1']])
# To Display one element in Column, df['ColumnName'][index]
# print(df['Country'][0])

# To Display one complete row with column, df.loc[index]
# print(df.loc[0])
# To Display multiple complete row with column, df.loc[[index1,index2]]
# print(df.loc[[0,1]])
print(df)
# To display one element in the df, df.iloc[rowindex,cloumnindex]
# print(df.iloc[0,0])
# To display one element in the df, df.iloc[rowindex,columnname]
# print(df.loc[0,'Country'])

# To Display suset of df, df.loc[[rowindex1,rowindex2],[colindex1,colindex2]]
# print(df.iloc[[0,1],[0,1]])
# To Display suset of df, df.loc[[rowindex1,rowindex2],[colname1,colname2]]
print(df.loc[[0,1],['Country','DummyValue1']])




# This will return Series
print(type(df['Country']))
# This will return df
print(type(df[['Country','DummyValue1']]))
# To add a new Cloumn to existing df
df['New']=[1,2,3,4,5,6]
# To drop a column, specify axis=1, Need to reassign it to existing df
# df = df.drop('New',axis=1)
# To drop a column, specify axis=1, This will modify existing df
# df.drop('New',axis=1,inplace=True)
# To drop a column, not required to specify axis=0, Need to reassign it to existing df
# df = df.drop(5,axis=0,inplace=True)
# To drop a column, This will modify existing df
df.drop(5,inplace=True)
# print(df)
# To get the df shape, Return type is tuple(rows,columns)
print(df.shape)

'''
mylist = MyList(df['Country'])
mylist.forEach(lambda var: print(var))
l = mylist
l.MyListMap(lambda var : var+",Country")
print(l)

l = list([1,2,3])
l = list(['Johnnnyyyyy','castor','troy'])
li = MyList(l)
#print(l.list1)
li.forEach(lambda var: print(var))
li.MyListMap(lambda var: var+"Hero")
li.MyFilter(lambda var: len(var)>12)
print(li)
'''