val = input("enter the number")
valu_int = float(val)
if(valu_int%2 ==0):
    print("even")
elif(valu_int%2 != 0 and valu_int>0):
    print("odd")
else:
    print("wrong input")