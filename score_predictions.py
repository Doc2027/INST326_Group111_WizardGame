def score_predictions(predicted_list, actual_list,):
    """ Calculates a score for each player based on how close their prediction
    was to the number of tricks they actually won.

    Rules:
    - If prediction matches actual: score = 20 + (10 * actual)
    - If prediction is wrong: score = -10 * the difference
    
    Parameters:
        predicted_list(list): Each player's predicted number of tricks.
        actual_list (list): Each player's actual tricks won
        

    Returns:
        A list of scores, one for each player
    """
    scores = []
    
    for i in range(len(predicted_list)):
        
        predicted = predicted_list[i]
        actual = actual_list[i]
        
        #Apply scoring rules
        if predicted == actual:
            base_points = 20
            bonus = 10 * actual
            score = base_points + bonus
        else:
            difference = abs(predicted - actual)
            penalty = difference * -10
            score = penalty
            
        scores.append(score)
        
        
    return scores

