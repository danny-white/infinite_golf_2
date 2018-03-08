import matplotlib.pyplot as plt
import numpy as np

def insert(x,y,func,anomaly):
    return [func[i] + anomaly[i] if i < y and i > x else func[i] for i in range(len(func))]
    # return func


sample = 800
x = np.arange(sample)
y = [0.5 + (0.001 * i) for i in x]
yp = y

import random
n = int(sample/3 + sample/2 * random.random())
m = int(sample/2 * random.random())
o = int(sample * 0.8 * random.random())



yp = insert(n,n+75, yp, [0.5 for i in range(len(yp))])
yp = insert(m,m+100, yp, [-0.5 for i in range(len(yp))])

yp = insert(o,o+100, yp, [-0.3 for i in range(len(yp))])

z = np.polyfit(x,yp,30)
p = np.poly1d(z)
plt.plot(x,[p(i) for i in x])
plt.plot(x, yp)
plt.gca().set_ylim([0,2])
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()

