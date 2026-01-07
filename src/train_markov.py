import pandas as pd 
from datetime import datetime 
from collections import defaultdict
from engagement import engagementBucket 

df = pd.read_csv("/Users/mayurkashyap/Desktop/ytShortsMarkov/data/SyntheticShortsHistory.csv")
times = []
for t in df["timestamp"]:
    times += [datetime.strptime(t, "%Y-%m-%d %H:%M:%S")]
genres = list(df["genre"])
states = []

for i in range(1, len(times)): 
    deltaTime = (times[i] - times[i-1]).total_seconds() 
    state = (genres[i], engagementBucket(deltaTime))
    states.append(state)

transitionCount = defaultdict(lambda: defaultdict(int)) ## without lambda every key would refer to the same thing 
for i in range(len(states) - 1): 
    transitionCount[states[i]][states[i+1]] += 1


transitionMatrix = {}
for currentState in transitionCount: 
    transitionMatrix[currentState] = {}
    nextStatesCount = transitionCount[currentState]
    totalTransitions = 0 
    for count in nextStatesCount.values(): 
        totalTransitions += count 
    for nextState in nextStatesCount: 
        count = nextStatesCount[nextState]
        prob = count / totalTransitions  
        transitionMatrix[currentState][nextState] = prob 

MODEL = transitionMatrix 

if __name__ == "__main__": 
    print("Number of states", (MODEL))
    

    



