import random 
from train_markov import MODEL 
from train_markov import genres
from engagement import engagement 

def simulate(startState, steps):
    state = startState
    print("START: ", state)
    for i in range(steps): 
        transitions = MODEL.get(state)
        nextStates = list(transitions.keys())
        probs = list(transitions.values())
        state = random.choices(nextStates, probs)
        state = state[0]
        print("->", state)


if __name__ == "__main__": 
    print("Here are the genres:" +  f'{set(genres)}')
    print("Here are the engagements: "  + f'{set(engagement)}')
    genreInput = input("Enter genre:  ")
    while genreInput not in genres:  
        print("Not a known genre")
        genreInput = input("Enter a known genre: ")
    engagementInput = input("Enter engagement: ")
    while engagementInput not in engagement: 
        print("Not a known engagement")
        engagementInput = input("Enter a known engagement: ") 
    stepsInput = int(input("Enter steps (integer): "))
    while type(stepsInput) != int: 
        print("Not an integer")
        stepsInput = input("Enter the number of steps: ")
    simulate((genreInput, engagementInput), stepsInput)

