import random 
# Card Class
# Author: Sara
# Purpose: Represent each card in the Wizard deck
class Card:
    def __init__(self, value, suit=None, kind="normal"):
       
        self.value = value       # Store numeric rank
        self.suit = suit         # Hearts, Diamonds, Clubs, Spades
        self.kind = kind         # "normal", "wizard", "jester"

        self.rank = value        

    def __str__(self):
        if self.kind == "wizard":
            return "Wizard"
        if self.kind == "jester":
            return "Jester"
        return f"{self.value} of {self.suit}"

# Deck Class
# Purpose: Its the deck, shuffle, deal, and flip top card
import random
class Deck:
    """Represents the full Wizard deck."""
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
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """Deal num_cards from top of deck."""
        hand = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return hand

    def flip_top_card(self):
        """Return, but do not remove the top card of the deck."""
        if len(self.cards) == 0:
            return None
        return self.cards[0]
    
# Computer Player Function
# Author: Sara
# Purpose: Computer Player

def computer_choose_card(hand, trick_cards, lead_suit, trump):
    """
    Choose a card for the computer player to play during a trick
    """
    def is_wizard(c): return c.kind == "wizard"
    def is_jester(c): return c.kind == "jester"
    def is_normal(c): return c.kind == "normal"

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
    """
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.hand = []
        self.score = 0

    def add_card(self, card):
        """Add a card to the player's hand."""
        self.hand.append(card)

    def play_card(self, trick_cards, lead_suit, trump):
        """Choose a card to play for this trick."""
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

    def human_choose_card(self, lead_suit=None, trump_suit=None):
        """Lets the human player choose a card from their hand."""
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

def determine_trump(round_number, total_rounds, flipped_card, dealer_choice=None):
    """
    Decide the trump suit for the round.
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
    """Prints trump suit to all players."""
    for p in players:
        if trump_suit is None:
            print(f"[{p.name}] Trump suit this round: NO TRUMP!")
        else:
            print(f"[{p.name}] Trump suit this round: {trump_suit}")
            
            
# Score Predictions
# Author: Ricardo
# Purpose: Figure out score

def score_predictions(predicted_list, actual_list):
    """
    Calculates score for each player based on predictions
    """
    scores = []
    for i in range(len(predicted_list)):
        predicted = predicted_list[i]
        actual = actual_list[i]
        if predicted == actual:
            score = 20 + 10 * actual
        else:
            score = -10 * abs(predicted - actual)
        scores.append(score)
    return scores         

# Determine Trick Winner
# Author: Daniel
# Purpose: Find who wins the trick

def determine_trick_winner(trick, trump_suit, lead_suit):
    """
    Returns the index of the winning card in the trick
    """
    def card_strength(card):
        if card.kind == "wizard":
            return 10_000
        if card.kind == "jester":
            return -1
        suit_score = 200 if card.suit == trump_suit else 100 if card.suit == lead_suit else 0
        return suit_score + card.rank

    winner_card = max(trick, key=card_strength)
    return trick.index(winner_card)

def get_lead_suit(trick):
    """Return the suit of the first normal card played, else None."""
    return next((card.suit for card in trick if card.kind == "normal"), None)

# Move Checking / Rule Enforcement
# Author: Ryan
# Purpose: Validate the card play

def check_move(card_played, player_hand, first_suit, trump_suit):
    if card_played not in player_hand:
        print("You don't have that card!")
        return False
    if card_played.kind in ("wizard", "jester"):
        return True
    if first_suit is None:
        return True
    card_suit = card_played.suit
    if card_suit == first_suit:
        return True
    has_led_suit = any(c.suit == first_suit for c in player_hand)
    if has_led_suit:
        print(f"You must play a {first_suit} if you have one!")
        return False
    return True

# Main Game Loop
# Purpose: Run the game

if __name__ == "__main__":
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
            if dealer.is_computer:
                dealer_choice = random.choice(["Hearts", "Diamonds", "Clubs", "Spades"])
                print(f"{dealer.name} (computer) chooses trump: {dealer_choice}")
            else:
                dealer_choice = input(
                    f"{dealer.name}, you are dealer! Choose trump suit (Hearts/Diamonds/Clubs/Spades): "
                )
                if dealer_choice not in ["Hearts", "Diamonds", "Clubs", "Spades"]:
                    dealer_choice = random.choice(["Hearts", "Diamonds", "Clubs", "Spades"])

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

        # Play each trick in this round
        for trick_number in range(round_number):
            print(f"\nTrick {trick_number + 1}")
            input("Press Enter to play this trick") 

            trick_cards = []

            # Lead plays first
            lead_card = human.play_card(trick_cards, lead_suit=None, trump=trump_suit)
            trick_cards.append(lead_card)
            lead_suit = get_lead_suit(trick_cards)

            # Computer plays
            comp_card = computer.play_card(trick_cards, lead_suit, trump_suit)
            trick_cards.append(comp_card)

            # Determine winner
            winner_index = determine_trick_winner(trick_cards, trump_suit, lead_suit)
            winner_player = players[winner_index]
            actual_tricks[winner_index] += 1
            print(f"{winner_player.name} wins the trick!")

        # Score this round
        round_scores = score_predictions(predictions, actual_tricks)
        for i, player in enumerate(players):
            player.score += round_scores[i]
            print(
                f"{player.name} predicted {predictions[i]}, won {actual_tricks[i]}, "
                f"score this round: {round_scores[i]}, total score: {player.score}"
            )

    # END OF GAME 
    print("\n*** Game Over Bye Bye :) ***")
    for player in players:
        print(f"{player.name} final score: {player.score}")