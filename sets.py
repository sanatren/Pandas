#a set is a unordered collection data type itrable,mutable and has no duplicate elements.

print(type({1}))

print(set([1,2,4,3,3,5]))

#define a empty set
set_var = set( ["thanos","thor","thala"])
print(set_var)
print(type(set_var))

var = {"thanos","thor","thala","bust"}
var2 =  {"thanos","thor","thala"}
print(type(var))

#print(var[2]) cannot access single element in sets.

var.add("ironmen")  #element added in order (sorted)
#var.clear() deletes all elements of set

print(var.intersection(var2)) #returns common elements
#print(var2.intersection_update(var)) #updates vals.

print(var.difference(var2)) #returns non common elements.

print(var2.issubset(var)) #checks if var2 is subset of var or not.




