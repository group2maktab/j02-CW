str1=input("please enter str1")
str2=input("please enter str 2")
newStr1 = str2[:] + str1[2:]
newStr2 = str1[:2] + str2[2:]
print(newStr1,newStr2)