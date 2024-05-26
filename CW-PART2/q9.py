s1=input("plz enter str : ")
s2=input("plz enter str : ")
index= len(s1) // 2
s3 = s1[:index] + s2 + s1[index:]
print(s3)
