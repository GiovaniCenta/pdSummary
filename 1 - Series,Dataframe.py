
#===========================================Series===========================================
#-> Array uni dimensional capaz de armazenar data de qualquer tipo(int,string,float,objetos,etc).O eixo X é referenciado como o índice
import pandas as pd
import numpy as np
#createSerie = pd.Series(data,index=index) 
#->data can be: python dict,scalar values,etc
#->indexis is a list o axis labels
#->Index must be the same size as data
#ex:
randomNumbers = pd.Series(np.random.randn(5), index = ['a','b','c','d','e'])
print(randomNumbers)
print(randomNumbers.index)
#Auto-Index
print(pd.Series(np.random.randn(5)))
#->Pandas supports non-unique index values.If a call for a method that doesnt accept non unique values if lifted, an exception will be raised

#->Series can be instantied from dicts
#->When the data is a dict, index is not passed, the series will be ordered by the order of insertion
abbreviationSeries = {'US': 'United States','BR': 'Brazil','UK':'United Kingdom'}
print(pd.Series(abbreviationSeries))

#NaN is the standard missing data marker used in andas
#ex-> Missing MX, returns NAN in the third index
print(pd.Series(abbreviationSeries,index=['BR','US','MX','UK']))

#If data is an scalar value, indexes must be provided, value will repeat to match the length of index
print(pd.Series(176.4,index=['h','e','l','l','o']))

#You can use series as array, via seriesname.array, can be useful if you need some operation w/o index
#The above will return a array-like, if you need an actual array uses seriesname.to_numpy()

#Series is like a fixed-size dicct that you can get and set values by index
abS = {'US': 'United States','BR': 'Brazil','MX':' ','UK':'United Kingdom','CO':'Col'}
abS['MX'] = 'Mexico'
abS['CO'] = 'Colombia'
#print('CO' in abS) #true
#print('FR' in abS) #false
print(abS)

#If a label is not contained an exception is raised, if you use get instead, will return none or specified default
#abS['FR'] #exception
print(abS.get('FR',np.nan))

#Usually is not necessary go through looping between values, series can also be passed into most numpy methods
print(np.exp(randomNumbers))

#Key difference between series and array is the operation between series automatically alling the data based on label,
#and you can write without giving consideration if the series involved have the same labels
#The result of an operation between unaligned series will have the union of indexes.
#If a label isnt found in either series, the result will be marked as NaN.That gives a ton of freedom and flexibility in data analysis
#Having a index label though the data is missing is important for not have a loss of information
#You can drop labels missing data via dropna function

#Series can have a name
s5 = pd.Series(np.random.randn(5), index = ['a','b','c','d','e'],name="Random")
s6 = s5.rename("Random2") #obs:s5 and s6 are different objects

#===========================================#===========================================#===========================================#===========================================#===========================================
#===========================================#===========================================#===========================================#===========================================#===========================================#===========================================#===========================================
#===========================================#===========================================#===========================================#===========================================#===========================================
#===========================================#===========================================#===========================================#===========================================#===========================================
##===========================================DATAFRAME===========================================#===========================================#===========================================


