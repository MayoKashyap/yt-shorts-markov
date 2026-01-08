import numpy as np 
import pandas as pd 
from train_markov import MODEL 

states = list(MODEL.keys())

stateIndex = {}
indexState = {}
i = 0 
for state in states: 
    stateIndex[state] = i 
    i += 1 # correspond each col  with a state 

markovMatrix = np.zeros((len(states), len(states)))
for currentState in MODEL: 
    i = stateIndex[currentState]
    for nextState in MODEL[currentState]: 
        j = stateIndex[nextState]
        prob = MODEL[currentState][nextState]
        markovMatrix[i][j] = prob  # correspond each row with a state 

dfMatrix = pd.DataFrame(markovMatrix, index = states, columns = states )
print(" ---- Transition Matrix ----- ")
print(dfMatrix.round(4))
dfMatrix.to_csv("transitionMatrix.csv")

#evalues + evectors 

eValues, eVectors = np.linalg.eig(markovMatrix.T)
print(" ---- Eigenvalues ---- ")
for value in eValues: 
    print(value.round(4))

#findAttractiveSteadyState

target = 0 
smallestDiff = abs(eValues[0] - 1) 
for k in range(len(eValues)): 
    diff = abs(eValues[k] - 1)
    if diff < smallestDiff: 
        smallestDiff = diff 
        target = k 
steadyState = eVectors[:, target]/eVectors[:, target].sum()

steadyStateDf = pd.DataFrame({"states": states, "Long Run Prob": steadyState}) 
steadyStateDf = steadyStateDf.sort_values(by = "Long Run Prob")

print(" ---- Attractive Steady-State Distribution --- ")
print(steadyStateDf)

 


    


