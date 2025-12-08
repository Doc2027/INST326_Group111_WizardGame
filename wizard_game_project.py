# This is the offical project file 

# Can you see this message??

# Determining Trick Winners 
def determine_trick_winner(trick, trump_suit, lead_suit):
    """ Selecting the winner of a trick in a wizard card game.

    Args:
        trick (list): A list of dictionaries representing the cards played in 
            the trick. Each dictionary has keys: 'type' (str), 'suit' (str),
            and 'rank' (int).
        trump_suit (str): The suit that is trump for the current round.
        lead_suit (str): The suit that was led in the trick.
    """

    # Helper scoring function for the max() key
    def card_strength(card):
        # Wizards beat everything
        if card["type"] == "wizard":
            return 10_000

        # Jesters lose to everything
        if card["type"] == "jester":
            return -1

        # Conditional expression → technique
        suit_score = (
            200 if card["suit"] == trump_suit else
            100 if card["suit"] == lead_suit else
            0
        )

        return suit_score + card["rank"]

    # Use max() with key → technique
    winner_card = max(trick, key=card_strength)

    return trick.index(winner_card)

def get_lead_suit(trick):
    """
    Determine the lead suit of the trick.

    Args:
        trick (list): list of card dictionaries representing a trick.

    Returns:
        str or None: the lead suit, or None if no normal cards appear.
    """

    # generator expression → technique
    return next(
        (card["suit"] for card in trick if card["type"] == "normal"),
        None
    )
