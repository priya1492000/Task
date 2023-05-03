#Run command -> python .\task_1.py

import random

def generate_outcome(prob_map):
    """
    Generates an outcome based on the probabilities given in the prob_map.
    The input prob_map is a list of dictionaries, where each dictionary has
    one outcome and its probability.
    """
    total_prob = sum(prob for d in prob_map for prob in d.values())

    if total_prob != 100:
        raise ValueError("Probabilities don't add up to 100%")

    # Generate a random number between 0 and 1
    rand_num = random.random()

    # Iterate over the outcomes and their probabilities,
    # and return the first outcome whose probability is greater than the random number.
    cumulative_prob = 0
    for outcome_prob in prob_map:
        outcome, prob = list(outcome_prob.items())[0]
        cumulative_prob += prob / 100
        if rand_num < cumulative_prob:
            return outcome

def print_outcome_with_frequency(prob_map, num_trials):
    """
    Tests the generate_outcome function by generating num_trials outcomes
    and printing the frequency of each outcome.
    """
    outcome_freq = {}

    #Iterate for no of trials time
    for i in range(num_trials):
        outcome = generate_outcome(prob_map)

        #Update outcome_freq dictionary with frequency
        if outcome in outcome_freq:
            outcome_freq[outcome] += 1
        else:
            outcome_freq[outcome] = 1
    
    #Add those outcomes which have 0 probability
    keys_with_zero_prob = [k for d in prob_map for k, v in d.items() if v == 0]
    for key in keys_with_zero_prob:
        outcome_freq[key] = 0

    #Print outcome and frequency for 1000 trial times
    for outcome, freq in sorted(outcome_freq.items()):
        print(f"{outcome}: {freq}")

if __name__ == "__main__":
    try:
        # Input 1:
        prob_map_1 = [{"Head": 35}, {"Tail": 65}]
        print("Coin probability outcome:")
        print_outcome_with_frequency(prob_map_1, 1000)

        # Input 2:
        prob_map_2 = [{1, 10}, {2, 30}, {3, 15}, {4, 15}, {5, 30}, {6, 0}]

        #Convert prob_map_2 to list of dict
        prob_map_2 = [{k: v} for [k, v] in prob_map_2]
        prob_map_2.pop()
        prob_map_2.append({6: 0})

        print("Dice probability outcome:")
        print_outcome_with_frequency(prob_map_2, 1000)
    except Exception as e:
        print("Error: ", e)
