import numpy as np
import matplotlib.pyplot as plt
y = []
x = []

with open("C:/Users/Owner/PycharmProjects/PatriotHacks2018/weight_data.txt") as f:
    data = f.read()
    for i in range[10]:
        x += data[i]
        y.append(data[i])

data = data.split('\n')
for i in range(10):
    x.append(i)



fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title")
ax1.set_xlabel('x label')
ax1.set_ylabel('y label')

ax1.plot(x,y, c='r', label='the data')

leg = ax1.legend()

plt.show()