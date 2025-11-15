#Sara Susa
def computer_choose_card(hand, trick_cards, lead_suit, trump):
    """
    Choose a card for the computer player to play during a trick

    Args:
        hand (list of Card): Cards currently in computer players hand
        trick_cards (list of Card): Cards already played in the current trick
        lead_suit (str or None): The suit of the first card played in this trick
        trump (str or None): The trump suit for this round

    Returns:
        Card: The card the computer player chooses to play
    """
    def is_wizard(c): return c.kind == "wizard"
    def is_jester(c): return c.kind == "jester"
    def is_normal(c): return c.kind == "normal"

    cards_of_lead = []
    for c in hand:
        if is_normal(c) and c.suit == lead_suit:
            cards_of_lead.append(c)

    # No lead suit computer leads
    if lead_suit is None:
        for c in hand:
            if is_jester(c):
                return c
        lowest = hand[0]
        for c in hand:
            if is_normal(c) and is_normal(lowest) and c.rank < lowest.rank:
                lowest = c
        return lowest

    # Must follow suit
    if len(cards_of_lead) > 0:
        smallest = cards_of_lead[0]
        for c in cards_of_lead:
            if c.rank < smallest.rank:
                smallest = c
        return smallest

    # Cannot follow suit so dump Jester
    for c in hand:
        if is_jester(c):
            return c

    # play lowest normal if other
    lowest = hand[0]
    for c in hand:
        if is_normal(c) and is_normal(lowest) and c.rank < lowest.rank:
            lowest = c
    return lowest

