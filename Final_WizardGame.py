import random 
# Card Class
# Author: Sara
# Purpose: Represent each card in the Wizard deck
class Card:
    """
    Represents a card in the Wizard deck.

    Attributes:
        value (int): Numeric rank of the card (1-13) or None for special cards.
        suit (str): Suit of the card ("Hearts", "Diamonds", "Clubs", "Spades") or None for special cards.
        kind (str): Type of the card: "normal", "wizard", or "jester".
        rank (int): Same as value, used for comparing normal cards.
    
    Args:
        value (int): Numeric rank of the card.
        suit (str, optional): Card suit.
        kind (str, optional): Type of card.

    Returns:
        None

    Side effects:
        None
    """
    def __init__(self, value, suit=None, kind="normal"):
       
        self.value = value       # Store numeric rank
        self.suit = suit         # Hearts, Diamonds, Clubs, Spades
        self.kind = kind         # normal, wizard, jester

        self.rank = value        

    def __str__(self):
        """
        Convert card to string representation.

        Args:
            None
        Returns:
            str: Human readable string for this card.
        Side effects:
            None
        """
        if self.kind == "wizard":
            return "Wizard"
        if self.kind == "jester":
            return "Jester"
        return f"{self.value} of {self.suit}"

# Deck Class
# Author: Everyone
# Purpose: Its the deck, shuffle, deal, and flip top card
import random
class Deck:
    """
    Represents the full Wizard deck.

    Attributes:
        cards (list of Card): The deck of cards.

    Args:
        None

    Returns:
        None

    Side effects:
        None
    """
    def __init__(self):
        self.cards = []

      
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit, "normal"))

        # Add Wizards (no rank, no suit)
        for _ in range(4):
            self.cards.append(Card(None, None, "wizard"))

        # Add Jesters (no rank, no suit)
        for _ in range(4):
            self.cards.append(Card(None, None, "jester"))

    def shuffle(self):
        """
        Shuffle the deck of cards.

        Args:
            None
        Returns:
            None
        Side effects:
            Shuffles self.cards in place
        """
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """
        Deal a number of cards from the top of the deck.

        Args:
            num_cards (int): Number of cards to deal.

        Returns:
            list of Card: Cards dealt from the top of the deck.

        Side effects:
            Removes the dealt cards from self.cards.
        """
        hand = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return hand

    def flip_top_card(self):
        """
        Return, but do not remove, the top card of the deck.

        Args:
            None

        Returns:
            Card or None: Top card of the deck or None if deck is empty.

        Side effects:
            None
        """
        if len(self.cards) == 0:
            return None
        return self.cards[0]
    
# Computer Player Function
# Author: Sara
# Purpose: Computer Player

def computer_choose_card(hand, trick_cards, lead_suit, trump):
    """
    Author: Sara
    Technique: List comprehension
    computer_choose_card
    
    Choose a card for the computer player to play during a trick.
    
    Args:
        hand (list of Card): Computer's current hand.
        trick_cards (list of Card): Cards already played in the trick.
        lead_suit (str): Suit that was led in this trick.
        trump (str): Current trump suit.

    Returns:
        Card: Chosen card to play.

    Side effects:
        None
    """
    def is_wizard(c): return c.kind == "wizard"
    def is_jester(c): return c.kind == "jester"
    def is_normal(c): return c.kind == "normal"
    
    
# list comprehension technique
    cards_of_lead = [c for c in hand if is_normal(c) and c.suit == lead_suit]

    
    if lead_suit is None:
        for c in hand:
            if is_jester(c):
                return c
        lowest = hand[0]
        for c in hand:
            if is_normal(c) and is_normal(lowest) and c.rank < lowest.rank:
                lowest = c
        return lowest

   
    if len(cards_of_lead) > 0:
        smallest = cards_of_lead[0]
        for c in cards_of_lead:
            if c.rank < smallest.rank:
                smallest = c
        return smallest


    for c in hand:
        if is_jester(c):
            return c


    lowest = hand[0]
    for c in hand:
        if is_normal(c) and is_normal(lowest) and c.rank < lowest.rank:
            lowest = c
    return lowest
  
# Player Class
# Author: Sara
class Player:
    """
    Represents a player in the Wizard game (human or computer).

    Attributes:
        name (str): Player's name.
        is_computer (bool): Whether the player is a computer.
        hand (list of Card): Cards currently in the player's hand.
        score (int): Total score of the player.

    Args:
        name (str): Player's name.
        is_computer (bool): Whether the player is a computer.

    Returns:
        None

    Side effects:
        None
    """
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.hand = []
        self.score = 0

    def add_card(self, card):
        """
        Add a card to the player's hand.

        Args:
            card (Card): Card to add.

        Returns:
            None

        Side effects:
            Adds a card to self.hand
        """
        self.hand.append(card)

    def play_card(self, trick_cards, lead_suit, trump):
        """
        Choose a card to play for this trick.

        Args:
            trick_cards (list of Card): Cards already played in the trick.
            lead_suit (str): Suit that was led.
            trump (str): Current trump suit.

        Returns:
            Card: Chosen card to play.

        Side effects:
            Removes chosen card from player's hand.
            Prints special messages for Wizard or Jester cards.
        """
        if self.is_computer:
            chosen = computer_choose_card(self.hand, trick_cards, lead_suit, trump)
        else:
            chosen = self.human_choose_card(lead_suit, trump)

        self.hand.remove(chosen)

        # special messages for Wizards and Jesters
        if chosen.kind == "jester":
            print(f"Oops! {self.name} played a Jester!")
        elif chosen.kind == "wizard":
            print(f"Wow! {self.name} played a Wizard!")
        else:
            print(f"{self.name} plays: {chosen}")

        return chosen

# Technique: Composition of two custom classes (Player + Card interaction)
    def human_choose_card(self, lead_suit=None, trump_suit=None): 
        """
        human_choose_card
        Author: Sara
        Technique: Composition of two custom classes (Player + Card interaction)
        
        Lets the human player choose a card from their hand.

        Args:
            lead_suit (str or None): Lead suit to follow
            trump_suit (str or None): Trump suit

        Returns:
            Card: Card selected by human

        Side effects:
            Interacts with user via input() and print()
        """
        while True:
            print("\nYour hand:")
            for index, card in enumerate(self.hand):
                print(f"{index}: {card}")  

            try:
                pick = int(input("Choose the number of the card you want to play: "))
                if 0 <= pick < len(self.hand):
                    chosen_card = self.hand[pick]

                    # Check if this is a legal move
                    if check_move(chosen_card, self.hand, lead_suit, trump_suit):
                        return chosen_card
                    else:
                        print(f"You must follow suit ({lead_suit}) if you have one!")
                else:
                    print(f"Invalid number. Enter a number from 0 to {len(self.hand)-1}.")
            except ValueError:
                print("Please enter a valid number.")



# Trump Suit Selection
# Author: Ian
# Purpose: Decide trump for the round

# optional parameter technique dealer_choice=none
def determine_trump(round_number, total_rounds, flipped_card, dealer_choice=None):
    """
    Author: Ian 
    Technique: 
    determine_trump(round_number, total_rounds, flipped_card, dealer_choice=None): Optional parameters
    announce_trump_to_players(players, trump_suit): F-strings containing expressions

    Decide the trump suit for the round.

    Args:
        round_number (int): Current round number
        total_rounds (int): Total rounds
        flipped_card (Card): Card flipped for trump
        dealer_choice (str or None): Dealer choice if Wizard flipped (optional parameter)

    Returns:
        str or None: Trump suit

    Side effects:
        None
    """
    if round_number == total_rounds:
        return None

    if flipped_card.kind == "wizard":
        return dealer_choice

    if flipped_card.kind == "jester":
        return None

    if flipped_card.kind == "normal":
        return flipped_card.suit

    return None

def announce_trump_to_players(players, trump_suit):
    
    """
    Prints trump suit for all players.

    Args:
        players (list[Player])
        trump_suit (str or None)

    Returns:
        None

    Side effects:
        Prints trump suit
    """
    for p in players:
        if trump_suit is None:
            print(f"[{p.name}] Trump suit this round: NO TRUMP!") # f-string with expression
        else:
            print(f"[{p.name}] Trump suit this round: {trump_suit}") # f-string with expression
            
            
# Score Predictions
# Author: Ricardo
# Purpose: Figure out score
def calculate_score(predicted, actual, base_points=20):
    """
    Calculate the score for a single player for one round.

    Author: Ricardo 
    Technique: Optional Parameters

    Rules:
        If predicted == actual:
              score = base_points + 10 * actual
        Otherwise:
              score = -10 * abs(predicted - actual)

    Args:
        predicted (int): Number of tricks the player predicted.
        actual (int): Number of tricks the player actually won.
        base_points (int, optional): Default is 20.
        
    Side Effects:
        None.

    Returns:
        int: Score earned by the player for the round.
    """
    if predicted == actual:
        return base_points + 10 * actual
    return -10 * abs(predicted - actual)


def score_predictions(predicted_list, actual_list, player_names):
    """
    Calculate scores for all players in a round and print which players predicted correctly.

    Author: Ricardo 
    Technique: Set Operations

    Side Effects:
        Prints the names of players who predicted correctly.

    Args:
        predicted_list (list[int]): Predictions for each player.
        actual_list (list[int]): Actual trick counts for each player.
        player_names (list[str]): Names of the players.

    Returns:
        list[tuple]: A list of (player_name, score) for each player.
    """
    
    if len(predicted_list) != len(actual_list) or len(predicted_list) != len(player_names):
        raise ValueError("All input lists must be the same length")

    scores = []
    correct_predictions = set()

    for i in range(len(player_names)):
        name = player_names[i]
        predicted = predicted_list[i]
        actual = actual_list[i]

        score = calculate_score(predicted, actual)
        scores.append((name, score))

        if predicted == actual:
            correct_predictions.add(name)
            
    if correct_predictions:
        print("Players who predicted correctly this round:", ", ".join(sorted(correct_predictions)))
    else:
        print("No players predicted correctly this round.")
        
    return scores


# Determine Trick Winner
# Author: Daniel
# Purpose: Find who wins the trick

def determine_trick_winner(trick, trump_suit, lead_suit):
    """
    Author: Daniel
    Techniques:
        Conditional expressions
        Use of a key function with max()
        
    Determine the winner of a trick in a Wizard card game.

    Args:
        trick (list[Card]): Cards played in the trick
        trump_suit (str or None): Trump suit for the round
        lead_suit (str or None): Lead suit of the trick

    Returns:
        int: Index of the winning card in trick

    Side effects:
        None
    """
    # Helper scoring function for the max() key
    def card_strength(card):
        """
        Score a card for trick comparison.

        Args:
            card (Card): Card to score

        Returns:
            int: Strength value of card

        Side effects:
            None
        """
        # Wizards beat everything
        if card.kind == "wizard":
            return 10_000

        # Jesters lose to everything
        if card.kind == "jester":
            return -1

        # Conditional expression: technique
        suit_score = (
            200 if card.suit == trump_suit else
            100 if card.suit == lead_suit else
            0
        )

        return suit_score + card.rank

    # Use max() with key: technique
    winner_card = max(trick, key=card_strength)

    return trick.index(winner_card)

def get_lead_suit(trick):
    """
    Determine the lead suit of the trick (first normal card).

    Args:
        trick (list[Card]): Cards played in the trick

    Returns:
        str or None: Lead suit or None if no normal cards appear

    Side effects:
        None
    """

    # generator expression: technique
    return next(
        (card.suit for card in trick if card.kind == "normal"),
        None
    )
    
# Move Checking / Rule Enforcement
# Author: Ryan
# Purpose: Validate the card play

class CardChecker:
    """
    Author: Ryan
    Techniques:
        Magic method (__contains__)
        Generator expression (used inside __contains__)

    CardChecker determines whether a card play is legally allowed 
    based on a player's hand and the lead suit.

    Args:
        hand (list[Card]): The players current hand.
        lead_suit (str or None): Suit that must be followed if any.

    Side Effects:
        None

    Returns:
        None
    """
    def __init__(self, hand, lead_suit):
        self.hand = hand
        self.lead_suit = lead_suit
    
    def __contains__(self, card):
        """
        Technique: Magic method (__contains__)
        
        Technique: Generator expression
        Uses a generator expression to check if the player has the lead suit:
        any(c.suit == lead_suit for c in hand)
        
        Args:
            card (Card): The card being tested for legality.

        Returns:
            bool: True if the card is a legal play, False otherwise.

        Side Effects:
            None
        """
        if card not in self.hand:
            return False
        if card.kind in ("wizard", "jester"):
            return True
        if self.lead_suit is None:
            return True
        if card.suit == self.lead_suit:
            return True
        
        # Generator expression
        return not any(c.suit == self.lead_suit for c in self.hand)


class MoveCheck:
    """
    Author: Ryan
    
    Wrapper that uses CardChecker to validate moves.

    Args:
        None

    Side Effects:
        Prints warning if illegal move is attempted.

    Returns:
        None
    """
    def __init__(self):
        self.checker = None
    
    def validate(self, card, hand, lead_suit):
        """
        Validate whether a card play is legal using CardChecker.

        Args:
            card (Card): The card played.
            hand (list[Card]): Players hand.
            lead_suit (str or None): Required suit to follow.

        Returns:
            bool: True if the move is legal, if not then False.

        Side Effects:
            Prints warning message if the move is illegal.
        """
        self.checker = CardChecker(hand, lead_suit)
        
        if card not in self.checker:
            if lead_suit:
                print(f"Must play {lead_suit} if you have it!")
            return False
        return True

move_check = MoveCheck()

def check_move(card_played, player_hand, first_suit, trump_suit):
    """
    Used to validate a move using the MoveCheck instance.

    Args:
        card_played (Card)
        player_hand (list[Card])
        first_suit (str or None)
        trump_suit (str or None)   

    Returns:
        bool: True if move is legal, if not then False 

    Side Effects:
        May print an invalid play warning
    """
    return move_check.validate(card_played, player_hand, first_suit)
# Main Game Loop
# Author: Everyone
# Purpose: Run the game

if __name__ == "__main__":
    """
    Run the Wizard card game with human and computer players.

    Args:
        None

    Returns:
        None

    Side effects:
        Prompts for player name and predictions
        Prints rounds, card plays, trick results, and scores
        Updates Player objects' hands and scores
    """
    import random

    # Ask for player name
    player_name = input("Enter your name: ")
    
    # Create and shuffle deck 
    deck = Deck()
    deck.shuffle()

    # Create players
    human = Player(player_name)
    computer = Player("Computer", is_computer=True)
    players = [human, computer]

    max_rounds = 5
    for round_number in range(1, max_rounds + 1):
        print(f"\n*** Round {round_number} ***")
        input("Press Enter to start this round.")  

        # Reset hands
        for player in players:
            player.hand = []

        # Deal cards
        for _ in range(round_number):
            for player in players:
                if deck.cards:
                    player.add_card(deck.cards.pop(0))

        # Determine dealer (rotates each round)
        dealer_index = (round_number - 1) % 2
        dealer = players[dealer_index]
        print(f"\n{dealer.name} is the dealer this round!")

        # Flip top card for trump
        flipped_card = deck.flip_top_card()
        if flipped_card:
            deck.cards.pop(0)
        print(f"Flipped card for trump: {flipped_card}")

        # Dealer chooses trump if Wizard is flipped
        dealer_choice = None
        if flipped_card.kind == "wizard":
            valid_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

            if dealer.is_computer:
                dealer_choice = random.choice(valid_suits)
                print(f"{dealer.name} (computer) chooses trump: {dealer_choice}")
            else:
                # Normalize player's input
                dealer_choice = input(
                    f"{dealer.name}, you are dealer! Choose trump suit (Hearts/Diamonds/Clubs/Spades): "
                ).strip().capitalize()

                # If still invalid, computer picks one
                if dealer_choice not in valid_suits:
                    print("Invalid choice, selecting a random suit for you.")
                    dealer_choice = random.choice(valid_suits)

        # Determine trump using Ian’s function
        trump_suit = determine_trump(round_number, max_rounds, flipped_card, dealer_choice)
        announce_trump_to_players(players, trump_suit)

        # Ask players for predictions
        predictions = []
        for player in players:
            if player.is_computer:
                pred = random.randint(0, round_number)
                predictions.append(pred)
                print(f"{player.name} predicts: {pred} tricks")
            else:
                while True:
                    try:
                        pred = int(input(f"{player.name}, predict number of tricks you will win (0-{round_number}): "))
                        if 0 <= pred <= round_number:
                            predictions.append(pred)
                            break
                        else:
                            print(f"Please enter a number between 0 and {round_number}")
                    except ValueError:
                        print("Please enter a valid number")

        # Initialize actual tricks won
        actual_tricks = [0 for _ in players]

        for trick_number in range(round_number):
            print(f"\nTrick {trick_number + 1}")
            input("Press Enter to play this trick") 

            trick_cards = []  # List to store the cards played this trick

            # Human plays first (lead)
            lead_card = human.play_card(trick_cards, lead_suit=None, trump=trump_suit)
            trick_cards.append(lead_card)

            # Determine the lead suit from the first normal card played
            lead_suit = get_lead_suit(trick_cards)

            # Computer plays
            comp_card = computer.play_card(trick_cards, lead_suit, trump_suit)
            trick_cards.append(comp_card)

            # Determine who wins the trick
            winner_index = determine_trick_winner(trick_cards, trump_suit, lead_suit)
            winner_player = players[winner_index]

            # Update the number of tricks each player has won
            actual_tricks[winner_index] += 1

            # Print result of the trick
            print(f"{winner_player.name} wins the trick!")

        # Score this round
        player_names = [p.name for p in players]
        round_scores = score_predictions(predictions, actual_tricks, player_names)

        for i, player in enumerate(players):
            name, score_value = round_scores[i]  
            player.score += score_value
            print(
                f"{player.name} predicted {predictions[i]}, won {actual_tricks[i]}, "
                f"score this round: {score_value}, total score: {player.score}"
            )

    # End of game 
    print("\n*** Game Over Bye Bye :) ***")
    for player in players:
        print(f"{player.name} final score: {player.score}")