import random
import pickle


t = 0
with open("weight_data.pkl", "rb") as file:
    delta = pickle.load(file)
with open("excel_data10.pkl", "rb") as file1:
    x = pickle.load(file1)

for i in len(delta):
    t += delta[i] * x[i][random.randint(1, 100)]
print(t)
