val=(input("enter multiple values"))
num1=[int(i) for i in val.split()]
print(num1)
num1.sort()
print(num1)
k=int(input("enter the kth smallest no"))
if k > 0 and k <= len(num1):
    print(f"The {k}th smallest element in the list is: {num1[k-1]}")
else:
    print("Invalid value of k.")