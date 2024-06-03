list=[11,2,45,8,12,16,21,10,2,12,12,10]
size=len(list)//3
lst1 = list[:size][::-1]
lst2 = list[size:2*size][::-1]
lst3 = list[2*size:][::-1]
print(lst1,lst2,lst3)