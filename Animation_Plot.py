import numpy as np
import matplotlib.pyplot as plt
import random 

heads_Tails = [0, 0]

for _ in range(1000):
    heads_Tails[random.randint(0, 1)] += 1
    plt.bar(['Heads', "Tails"], heads_Tails, color=['red', 'blue'])
    plt.pause(0.001)
plt.show()