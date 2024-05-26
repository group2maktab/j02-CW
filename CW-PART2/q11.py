s1 = input("plz enter str : ")
s2 = input("plz enter str : ")
set1 = set(s1)
set2 = set(s2)
if set1.issubset(set2):
    print("True")
else:
    print("False")
