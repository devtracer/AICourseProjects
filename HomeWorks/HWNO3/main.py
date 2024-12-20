import numpy as np
import math

a = np.arange(1, 65)

b = np.array([math.sin(i) for i in a])

c = np.linspace(1, 100, 30, dtype=np.float16)

d = np.array(124 - i for i in range(0, 126))


print(d)