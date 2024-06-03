my_tuple = (2, "Python", (3, 5), [2, "Python", (3, 5)], "Maktab")
if len(my_tuple) % 2 != 0:
    my_tuple = my_tuple[:-1]
dict = {}
for i in range(0, len(my_tuple), 2):
    dict[my_tuple[i]] = my_tuple[i+1]  
print(dict) 
    
