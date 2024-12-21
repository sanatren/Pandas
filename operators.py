#type(True)
a = "sanatan"
b = "sanatan"
print(id(a))#id functions shows alloted memory of variable
print(id(b))

print(a is b)#true
print(a is not b)#false

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)#false (diff allocation bc var name)
print(list1 is not list2)#true

print(48/2.5)#division

print(48//2.5)#true or integer division