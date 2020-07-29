
# #===========================================Series===========================================
# #-> Array uni dimensional capaz de armazenar data de qualquer tipo(int,string,float,objetos,etc).O eixo X é referenciado como o índice
# import pandas as pd
# import numpy as np
# #createSerie = pd.Series(data,index=index) 
# #->data can be: python dict,scalar values,etc
# #->indexis is a list o axis labels
# #->Index must be the same size as data
# #ex:
# randomNumbers = pd.Series(np.random.randn(5), index = ['a','b','c','d','e'])
# print(randomNumbers)
# print(randomNumbers.index)
# #Auto-Index
# print(pd.Series(np.random.randn(5)))
# #->Pandas supports non-unique index values.If a call for a method that doesnt accept non unique values if lifted, an exception will be raised

# #->Series can be instantied from dicts
# #->When the data is a dict, index is not passed, the series will be ordered by the order of insertion
# abbreviationSeries = {'US': 'United States','BR': 'Brazil','UK':'United Kingdom'}
# print(pd.Series(abbreviationSeries))

# #NaN is the standard missing data marker used in andas
# #ex-> Missing MX, returns NAN in the third index
# print(pd.Series(abbreviationSeries,index=['BR','US','MX','UK']))

# #If data is an scalar value, indexes must be provided, value will repeat to match the length of index
# print(pd.Series(176.4,index=['h','e','l','l','o']))

# #You can use series as array, via seriesname.array, can be useful if you need some operation w/o index
# #The above will return a array-like, if you need an actual array uses seriesname.to_numpy()

# #Series is like a fixed-size dicct that you can get and set values by index
# abS = {'US': 'United States','BR': 'Brazil','MX':' ','UK':'United Kingdom','CO':'Col'}
# abS['MX'] = 'Mexico'
# abS['CO'] = 'Colombia'
# #print('CO' in abS) #true
# #print('FR' in abS) #false
# print(abS)

# #If a label is not contained an exception is raised, if you use get instead, will return none or specified default
# #abS['FR'] #exception
# print(abS.get('FR',np.nan))

# #Usually is not necessary go through looping between values, series can also be passed into most numpy methods
# print(np.exp(randomNumbers))

# #Key difference between series and array is the operation between series automatically alling the data based on label,
# #and you can write without giving consideration if the series involved have the same labels
# #The result of an operation between unaligned series will have the union of indexes.
# #If a label isnt found in either series, the result will be marked as NaN.That gives a ton of freedom and flexibility in data analysis
# #Having a index label though the data is missing is important for not have a loss of information
# #You can drop labels missing data via dropna function

# #Series can have a name
# s5 = pd.Series(np.random.randn(5), index = ['a','b','c','d','e'],name="Random")
# s6 = s5.rename("Random2") #obs:s5 and s6 are different objects

#===========================================#===========================================#===========================================#===========================================#===========================================
#===========================================#===========================================#===========================================#===========================================#===========================================#===========================================#===========================================
#===========================================#===========================================#===========================================#===========================================#===========================================
#===========================================#===========================================#===========================================#===========================================#===========================================
#===========================================DATAFRAME======================================================================================#===========================================

import pandas as pd
import numpy as np
#Dataframe is a 2 dimentional ds, most commonly used pandas object
#Along with data, you can optionally pas index(row) and columns(columns labels)
#If index labels (axis) are not passed they will constructed from the input data based on common sense rules
#ex:
# df={"a":[1,2,3,4],
#     "b":[4,7,8,9],
#     "hi":["h","i","j","a"]} #must be the same length
# print(pd.DataFrame(df,index=["A","B","C","D"]))
# print(pd.DataFrame(df,columns=["10","11","12"]))
# print(pd.DataFrame(df)) 

#creating from a list of dicts
#data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
#print(pd.DataFrame(data2))

#If you pass orient='index', the keys will be the row labels. In this case, you can also pass the desired column names:

data3=pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),
                       orient='index', columns=['one', 'two', 'three'])
#print(data3)
#selecting columns
#print(data3['one'])
#print(data3['two']*data3['two'])
data3['f'] = data3['two'] > 2 #willc reate new columns "f" with true or false if the number in column two is biger than 2
del data3["three"]
two=data3.pop("two")
print(data3)
print(f'\nTwo popped column: \n{two}\n\n')
data3["newCol"] = "newValue" #will add one new column with all values="newValue"
#print(data3)
#when inserting a series that does not have the same index as the DF index will add NaN in those indexes
data3["newCol2"] = data3["one"][:1] #will select the first  row of data3 one column
#print(data3)
#you can insert after some column but the lenght must match the lenght of the DF's index
data3.insert(1,"insnewCol",[9,3])
#print(data3)

data3.insert(4,"divide",(data3["one"]/data3["insnewCol"]))
#print(data3)

print(data3.assign(divide=lambda x: (x['insnewCol'] / x['one']))) #will assign column divide to be a division between two columns via lambda function
#Passing a callable, as opposed to an actual value to be inserted, is useful when you don’t have a reference to the DataFrame at hand
print("\n")

#indexing/selection
print(data3["divide"]) #select column
print("\n")
print(data3.loc["A"]) #select  row A
print("\n")
print(data3.iloc[0]) #select first element
print("\n")
print(data3[0:1]) 
selectColumns=data3.iloc[:,1:3] #will select columns 2,3 , first argument of iloc is the number of rows you want to select 

#Data alignment: automatically align on both the columns and the index, the result object will be the union
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
df3=df+df2
print(df3)

#can do mathematical operations 
print(df3*5+2)

#also can do boolean operations
#print(df & df2)
#print(df | df2)

#Console display
print("\n\n")
print(data3.to_string())
#can change how much to print on a single row via display.width
pd.set_option('display.width',10) #default=80
print(pd.DataFrame(np.random.randn(4,10)))
#can adjust the max width of the individual columns by setting display.max_coldwidth
pd.set_option('display.max_coldwidth',10)





