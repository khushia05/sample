sequence=input("enter the numbers").split()
s=[int(i) for i in sequence]
ap=False
common_diff=s[1]-s[0]
for i in range(len(s)):
    if s[i]-s[i-1]==common_diff:
        ap=True
        break
if ap==True:
    print("sequence in ap")
else:
    print("not")    

