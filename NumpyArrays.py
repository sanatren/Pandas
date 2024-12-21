#import numpy library to create array.

import numpy as np

#creating array
lst = [1,2,3,4,5]
arr = np.array(lst)

print(type(arr))#type is numpy array..

#creating multidimentional array

list1 = [1,2,3,4,5,]
list2 = [6,7,8,9,10]
list3 = [11,12,13,14,15]

arr1 = np.array([list1,list2,list3])
print(arr1)

#[[ 1  2  3  4  5]  here no. of brackets in starting and ending shows the dimensions of array
# [ 6  7  8  9 10]
# [11 12 13 14 15]]

print(arr1.shape) #displays the no. of rows and columns in array

print(arr1[1][2]) #indexing

##range index in arrays
print(arr[1:3]) #elements from index 1 to 3 will print out
print(arr[-1])#retuns last element cuz indexing from last.
print(arr[:-1])#all elements will be printed leavig last element
print(arr[::-1])#reverse the arrangement of elements in arrays

print(arr[::-2])#reverse the array by jumping the indexes given in argument 
#output = [5 3 1]

#range indexing in 2d arrays 

print(arr1[:,1])#selecting 1 column in every row
print(arr1[1:,1:3])#selecting elements from row 1 till end and selecting columns between 1 and 3 in rows
print(arr1[1:,3:])

#camparing elements in array
print(arr<2)#checking which element bigger then 2

print(arr1.reshape(5,3))#reshapes the array in desired form but in bound of range of rows and columns

#mechanism to create array
print(np.arange(1,10,1))#creates the array to given range 10 
print(np.arange(1,20,2))#third argument jumps the elements between the range 

print(np.arange(1,11,1).reshape(2,5))#creating and shaping them at same time

#operations in array
print(arr1 * arr1)#multipluing each elemnt by itself
print(arr*2)#now multiplying by 2

#functions

print(np.random.randint(10,50,5))#creating array of size 4 between 10 and 50
print(np.random.randint(10,50,4).reshape(2,2))

