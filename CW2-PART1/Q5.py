from collections import Counter
my_dict = {'T_shirt': 45.50, 'hat':55 , 'back pack':24 ,'pants': 35, 'sneakers': 41.30,}
k = Counter(my_dict)
high = k.most_common(3)
print("Initial Dictionary:")
print(my_dict, "\n")
print("Dictionary with 3 expensive items:")
print("Keys: Values")
for i in high:
    print(i[0]," :",i[1]," ")
