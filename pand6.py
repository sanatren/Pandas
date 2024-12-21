#Pickle in Python is primarily used in serializing and deserializing a Python object structure. In other words, 
#it's the process of converting a Python object into a byte stream to store it in a file/database, 
#maintain program state across sessions, or transport data over the network.
import seaborn as sns;
import pickle
import pandas as pd

df =sns.load_dataset('tips')
print(df.head())

filename = 'file.pkl' #creating a name for pickle file;
filename2 = 'db.pkl'
#serialization of dataframe (pickling)
pickle.dump(df,open(filename,'wb'))#using the open function to open file and opening in write fron using WB

#unserialization of dataframe (unpickling)
pickle.load(open(filename,'rb')) #here use load function to umpickle data

dic = {'fname':"sanatan" , 'Lname':"khemariya"}

pickle.dump(dic,open(filename2,'wb'))

print(pickle.load(open(filename2,'rb')))

