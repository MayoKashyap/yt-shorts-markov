from train_markov import MODEL 

def predictNextDistribution(state): 
    return MODEL.get(state, {})


if __name__ == "__main__": 
    state = ("comedy", "zombie")
    probs = predictNextDistribution(state)
    for state, prob in probs.items(): 
        print(f'{state} -> {prob}')


