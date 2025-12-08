

class Card:
    """
    Represents a single card in the Wizard game.

    Attributes:
        suit (str): The suit of the card like Hearts or Spades 
        rank (int): The number rank of the card 1-13 for normal cards
        kind (str): Type of the card: "normal", "wizard", or "jester"

    """
    def __init__(self, suit, rank, kind="normal"):
        self.suit = suit
        self.rank = rank
        self.kind = kind

    def __str__(self):
        if self.kind == "wizard":
            return "Wizard"
        if self.kind == "jester":
            return "Jester"
        return f"{self.rank} of {self.suit}"
    


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




class Player:
    """
    Represents a player in the Wizard game (human or computer).

    Attributes:
        name (str): Player's name.
        is_computer (bool): Whether the player is a computer.
        hand (list of Card): Cards currently in the player's hand.

    """
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.hand = []

    def add_card(self, card):
        
        """ Add a card to the players hand """
        
        self.hand.append(card)

    def play_card(self, trick_cards, lead_suit, trump):
        """
        Choose a card to play for this trick.
        For computer players calls computer_choose_card
        For human players calls human_choose_card

        Args:
            trick_cards (list of Card): Cards already played in the trick.
            lead_suit (str or None): The suit of the first card in the trick.
            trump (str or None): Trump suit for the round.

        Returns:
            Card: The card chosen to play removed from hand

        """
        if self.is_computer:
            chosen = computer_choose_card(self.hand, trick_cards, lead_suit, trump)
            print(f"{self.name} plays: {chosen}")
        else:
            chosen = self.human_choose_card()
        self.hand.remove(chosen)
        return chosen

    def human_choose_card(self):
        """
        Lets the human player choose a card from their hand
        Displays the hand, prompts user for input,
        and validates the choice

        Returns:
            Card: The card chosen by the human player.

        """
        while True:
            print("\nYour hand:")
            
            index = 0
            for card in self.hand:
                print(index, card)
                index += 1

            try:
                pick = int(input("Choose a card number: "))
                if 0 <= pick < len(self.hand):
                    print(f"You play: {self.hand[pick]}")
                    return self.hand[pick]
                else:
                    print("Invalid choice, Please try again :)")
            except ValueError:
                print("Please enter a number: ")

