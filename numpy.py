import numpy as np
a=np.array([0,1])
b=np.array([9,8])
c=a
d=b.copy()
d[0]=8
print(b)
print(d)