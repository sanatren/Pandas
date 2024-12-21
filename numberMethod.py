print(abs(-10))#mod of number

#pow() return power value asked for number

print(pow(-5,5))
print(pow(5,5))

import math  #math library

#ceil()
print(math.ceil(43.1))#returns the next largest number if value is in float or >0
print(math.ceil(-43.1))#vice versa in negetive number

#floor()
print(math.floor(43.1))#vice versa of ceil return previous smallest
print(math.floor(-43.1)) #vice ver...

#exp()  returns exponential of a number
#ex 7 ^ 7
print(math.exp(7))
print(math.exp(-7))

#fabs() same as abs() gives float value

#log(x) returns logrithmic value of x

print(math.log(10))
print(math.log(100)) #by default the base is 2 

print(math.log10(100)) 
print(math.log10(100)) #base 10

# max() find the max number in a given range

print(max(10,12,14,77))

#min() vice versa of max

print(min(10,11,9,-1))

#sqrt() returns square root of number and cannot use neg(-) number
print(math.sqrt(16)) 

#triggnometric functions

print(math.sin(0))
print(math.cos(32))
print(math.tan(45))

#hupot() returns hypotanese of triangle
#inputs will be base and perpendiculer

print(math.hypot(2,4))

#modf()  returns the fractional and integer parts of x in a two item tuple.
print(math.modf(12.3))