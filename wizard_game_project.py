# This is the offical project file 

# Can you see this message??

# Determining Trick Winners 
def determine_trick_winner(trick, trump_suit, lead_suit):
    """ Selecting the winner of a trick in a wizard card game.
    Args:
        trick (list): A list of dictionaries representing the cards played in 
            the trick.Each dictionary has keys: 'type' (str), 'suit' (str),
                and 'rank' (int).
        trump_suit (str): The suit that is trump for the current round.
    """

    # 1. check for wizard
    i = 0
    while i < len(trick):
        if trick[i]["type"] == "wizard":
            return i
        i += 1

    # 2. collect trump cards
    trump_winner = None
    i = 0
    while i < len(trick):
        card = trick[i]
        if card["type"] == "normal" and card["suit"] == trump_suit:
            if trump_winner is None or card["rank"] > trick[trump_winner]["rank"]:
                trump_winner = i
        i += 1

    if trump_winner is not None:
        return trump_winner

    # 3. collect lead suit cards
    lead_winner = None
    i = 0
    while i < len(trick):
        card = trick[i]
        if card["type"] == "normal" and card["suit"] == lead_suit:
            if lead_winner is None or card["rank"] > trick[lead_winner]["rank"]:
                lead_winner = i
        i += 1

    if lead_winner is not None:
        return lead_winner

    # 4. no wizards, no trumps, no lead suit → first jester wins
    i = 0
    while i < len(trick):
        if trick[i]["type"] == "jester":
            return i
        i += 1

    return None
