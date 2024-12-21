print(type({1:"a"}))

print(dict(name = "krish" , age = 31 , last_name = 'Naik'))

dict1 = {"car1" : "Audi" , "car2" : "BMW" , "car3" : "buggatti"}

print(dict1["car1"])#accessing a single element in dict...

print(dict1.keys())# returns car1 etc ..
print(dict1.values())# returns values like BMW etc ...

for i in dict1.values():#dict.keys()
    print(i)#returns values 

for i,j in dict1.items():#accessing both keys and vals same time.
    print(i," ",j)

dict1["car4"] = "Bentley" #adding a new element in dict.

for i in dict1.values():#dict.keys()
    print(i)

