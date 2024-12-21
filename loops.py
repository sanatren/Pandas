lst = [1,2,3,4,5,6,7,8,9]
#sum of all elements in list
sum1 = 0
for j in lst:
    sum1= sum1 +j
print(sum1)
#sum of the odd and even number
even_sum=0
odd_sum = 0

for k in lst:
    if(k%2==0):
        
        even_sum = even_sum +k
    elif(k%2!=0 and k > 0):
       
        odd_sum = odd_sum + k
print("even sum is {}".format(even_sum))
print("odd sum is {}".format(odd_sum))

l = 0   
while(l<= 10):
    if(even_sum%2 == 0):
        even_sum = even_sum +1
        print("even")
        
        
    else:
        print("odd")
    l = l+1
