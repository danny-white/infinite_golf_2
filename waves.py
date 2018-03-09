import matplotlib.pyplot as plt
import numpy as np
import random, time

def insert_bump(beginning, func, magnitude, length):
    return insert(beginning, beginning + length, func, [magnitude for i in range(len(func))])

def insert(x,y,func,anomaly):
    return [func[i] + anomaly[i] if i < y and i > x else func[i] for i in range(len(func))]
    # return func

def moving_average(func, points):
    avg = lambda lst: sum(lst)/len(lst)
    
    ret = []
    for i in range(1, len(func)+1):
        first = max(0,i-points)
        ret.append(avg(func[first:i]))
    return ret

curves = []
sample = 1000 #scale is 0,2 for y axis and 0,1000 for the x axis


def build_curve(sample, slope):
    x = np.arange(sample)
    offset = 1 - (slope * sample) / 2 # 1 is the middle of the screen
    
    y = [offset + (slope * i) for i in x] #

    hole_offset = sample/5
    anomalies = []
    num_anomalies = 5
    for i in range(num_anomalies):
        anomalies.append(int(hole_offset*i + sample/5 * random.random()))

    # insert anomalies, they should be a max of 10% of len in width, they should be max of 20% of len in height
    # there should be a max of 5 anomalies on the golf course, they should be relatively spread out, so they dont stack up and explode
    # give each one 1/5 of total range 
    for i in anomalies:
        direc = 1 if random.random() > 0.5 else -1
        mag = random.random() * 0.4 + 0.3
        length = 0.2 * sample * random.random()
        y = insert_bump(i,y,direc * mag, length)
    
    p = np.poly1d(np.polyfit(x,y,30))
    return x, moving_average([p(i) for i in x], 150)
    


# plt.plot(x,[p(i) for i in x])
# plt.plot(x,moving_average([p(i) for i in x], 150))



plt.ion()

while True:
    plt.gca().set_ylim([0,2])
    plt.xlabel('sample(n)')
    plt.ylabel('voltage(V)')
    c = build_curve(1000, 0.002 * random.random() - 0.001)
    if max(c[1]) > 1.7 or min(c[1]) < 0.3 : # if its too wild
        continue
    if max(c[1]) - min(c[1]) < 0.8 : # if its not wild enough
        continue
    plt.plot(c[0], c[1])
    plt.pause(0.1)
    plt.clf()



# for p in curves:
    
#     a = plt.plot(x,moving_average([p(i) for i in x], 150))
    
#     time.sleep(0.5)
#     a.clear()
# plt.plot(x, y)


