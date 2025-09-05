import numpy as np
x = np.array([1,2,3,4])
print(x.dtype)
new = np.float32(x)
print(new.dtype)
new_ = np.int_(new)
print(new_.dtype)