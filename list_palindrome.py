val=(input("enter multiple values"))
num1=[int(i) for i in val.split()]
print(num1)
new_lst = num1[::-1]
if num1== new_lst:
    print("list is palindrome")
else:
    print("not")    
