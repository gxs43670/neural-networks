import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
data = pd.read_csv('data.csv')
print (data)

print ("-------------------------------------------------")
print (data.mean())

print ("-------------------------------------------------")
print (data.median())

print ("-------------------------------------------------")
print (data.mode())

print ("-------------------------------------------------")
print (data.std())

print ("-------------------------------------------------")
print (data.var())

print ("-------------------------------------------------")
print (data.isnull().sum())

print ("-------------------------------------------------")
data['Calories'] = data['Calories'].fillna(data['Calories'].mean())

print ("-------------------------------------------------")
print (data.isnull().sum())

print ("-------------------------------------------------")
result = data[['Duration','Maxpulse']].agg(['min','max','count','mean'])
print (result)

print ("-------------------------------------------------")
d1 = data[data['Calories'].between(500,1000)]
print (d1)

print ("-------------------------------------------------")
d2 = data[(data['Calories']>500) & (data['Pulse']<100)]
print (d2)

print ("-------------------------------------------------")
data_modified=data.drop('Maxpulse',axis=1)
print (data_modified)

print ("-------------------------------------------------")
data.drop('Maxpulse',axis=1)
data["Calories"]=data["Calories"].astype(float).astype(int)
print (data)

print ("-------------------------------------------------")
plot = data.plot.scatter(x="Duration",y="Calories")
print ("plot: ", plot)