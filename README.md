# Modeling YouTube Shorts Scrolling with Markov Chains

## Overview
This project models my YouTube Shorts scrolling behavior using a Markov chain.
Each scroll event is treated as a transition between states defined by the
type of content being viewed and the user’s level of engagement.

The goal is to understand how my scrolling behavior evolves over time and what
patterns dominate user attention in the long run.

## Data
The dataset consists of synthetic YouTube Shorts watch history containing:
- Timestamps of scroll events
- Content genres

User engagement is inferred from the time between consecutive scrolls and
bucketed into five levels:
- fast
- normal
- slow
- linger
- zombie


## State Representation
Each state represents a combination of:
- Content genre (e.g. comedy, pets, music)
- Engagement level inferred from scroll timing

This representation captures what content is being consumed and how
the user is interacting with it.



## Transition Modeling
Transition probabilities are learned directly from scrolling data.
For each state, the model estimates how likely the user is to transition to
every other state on the next scroll.

These probabilities form a transition matrix that encodes scrolling dynamics
across content and engagement levels.



## Attractive Steady-State Results
When the transition model is applied repeatedly, the system converges to a
stable distribution over states. This distribution represents how attention
is allocated in the long run, regardless of the initial scrolling state.

### Top Long-Run States
The highest-probability steady-state outcomes are:

- (comedy, normal): 19.2%
- (pets, normal): 15.0%
- (music, normal): 13.5%
- (comedy, fast): 13.0%
- (pets, fast): 9.6%

All zombie states combined account for less than 3% of the steady-state
distribution.



## Interpretation
The model predicts that long-run scrolling behavior stabilizes around
moderate engagement rather than extreme disengagement.

Comedy content emerges as the strongest attention attractor, followed by
pets and music. While fast scrolling occurs frequently, attention does not
collapse into prolonged zombie scrolling.

This suggests that the structure of short-form content encourages sustained,
repeatable engagement rather than complete attentional burnout.



## Project Structure
- `src/train_markov.py` — builds the transition model from data
- `src/analyze_markov.py` — analyzes long-run behavior
- `results/transition_matrix.csv` — learned transition probabilities
- `results/steady_state_distribution.csv` — long-run attention distribution

