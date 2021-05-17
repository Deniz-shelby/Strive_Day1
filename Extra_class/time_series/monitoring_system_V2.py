from os import pread
import random
import pandas as pd
from time import time, sleep

[1,0,1,1,1]

df = pd.read_csv("./heart_attack.csv")

predictions = []

    
for i in range(df.shape[0]):
    sleep(0.1)
    pred = random.randrange(0,10)
    print(df.values[i])
    if pred < 9:
        predictions.append(0)
    else:
        predictions.append(1)

    if len(predictions) == 5:
        cont  = 0
        for p in predictions:
            if p == 0:
                cont += 1
        if cont >= 4:
            print("HEART ATTACK")
            sleep(2)
            predictions = []
            print(predictions)
            continue
        predictions.remove(predictions[0])
'''
#start = time()

while True:

    #end = time()
    sleep(1)
    #if end - start > 1:
    print("MAKING A PREDICTION")
    pred = random.randrange(0,10)

    if pred < 8:
        predictions.append(0)
    else:
        predictions.append(1)

    if len(predictions) == 5:
        cont  = 0
        for p in predictions:
            if p == 1:
                cont += 1
        if cont >= 4:
            print("HEART ATTACK")
        predictions.remove(predictions[0])
    

        #start = end
'''





