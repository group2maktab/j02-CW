letters = 0
digits = 0 
symb = 0
str = input("enter str: ")
for i in str :
    if "A" <= i <= "z":
        letters +=1
    elif "0" <= i <= "9":
        digits +=1
    else:
        symb +=1
print("letters = " , letters)
print("digits = " , digits)
print("symb = " , symb)