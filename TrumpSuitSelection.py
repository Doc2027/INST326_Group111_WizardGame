def determine_trump(round_number, total_rounds, flipped_card, dealer_choice=None):
    """
        Decides what the trump suit is for the round
    """
    if round_number == total_rounds:
        return None
    
    if flipped_card["type"] == "number":
        return flipped_card["suit"]
    
    if flipped_card["type"] == "jester":
        return None
    
    if flipped_card["type"] == "wizard":
        return dealer_choice
    
    return None

def announce_trump_to_players(players, trump_suit):
    """
        Tell each player what the trump suit is.
    """
    for p in players:
        if trump_suit is None:
            print(f"[{p}] Trump suit this round: NO TRUMP!")
        else:
            print(f"{p} Trump suit this round: {trump_suit}")