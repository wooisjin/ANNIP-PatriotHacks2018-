import math
import random
import pickle
import simplejson


def sigmoid(x):
  return 1 / (1 + math.exp(-x))

#Accuracy Counter of previous 50 tries
accuracy1 = [0]
accuracy2 = [0]
#Empty Array for the weights
delta = []

#Start of a parameter counter
z = 0
while z <= (99999):
    #Random number generator of weight. Floats between 0 & 1 to two decimal places
    delta.append(round(random.uniform(0, 1), 2))
    z += 1

#Arbitrary float between 0 & 1 used to calculate change in Delta
alpha = 0.2
bias = 1

#Start of Machine Learning Process
g = 0
while g <= 10000: #10000 is an arbitrary value for counting when to stop
    t_1 = 0
    t = 0 #Introduce variable <t>: Prediction Value
    #Opens ".txt" files for munipulation of data
    f1 = open("excel_data10.pkl", "rb")
    f2 = open("anskey.pkl", "rb")

    x = pickle.load(f1) #Input data
    y = pickle.load(f2) #Answer Data


    #Calculates the Prediction for one cycle
    for i in range(len(x)):
        try:
            t_1 += delta[i] * x[i][g]
        except IndexError:
            pass
    if t_1 > 0:
        t = 1
    else:
        t = 0
    #Sigmoid function for a value between 0 & 1
    #Calculating the change of delta for the weights
    #print("The Cost is {}".format(y[g]-t))
    if abs(y[g]-t) == 1:
        accuracy1.append(1)
    else:
        accuracy2.append(0)
    accuracy = 100 - (round(100 * ((len(accuracy1) / len(accuracy2))), 4))
    print("{}%".format(accuracy))
    for i in range(len(x)):
        try:
            delta[i] += (alpha * (y[g] - t) * x[i][g])

        except IndexError:
            pass
    #Store value of weights unto ".txt"
    with open("weight_data.pkl", "wb") as file_pkl:
        pickle.dump(delta, file_pkl)
    with open("weight_data.txt", "w") as file_txt:
        simplejson.dump(delta, file_txt)
    #Close all file processes
    g += 1
    if len(accuracy1) > 30:
        accuracy1 = accuracy1[-30:]
