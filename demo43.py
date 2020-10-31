import  numpy as np
a1 = np.array([1,2,3])
a2 = a1
a3 = a1.copy()
print(a1,hex(id(a1)))
print(a2,hex(id(a2)))
print(a3,hex(id(a3)))
a1 += 10
print(a1,a2,a3)