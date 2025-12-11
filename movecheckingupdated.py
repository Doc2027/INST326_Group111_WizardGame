class CardChecker:
    def __init__(self, hand, lead_suit):
        self.hand = hand
        self.lead_suit = lead_suit
    
    def __contains__(self, card):
        if card not in self.hand:
            return False
        if card.kind in ("wizard", "jester"):
            return True
        if self.lead_suit is None:
            return True
        if card.suit == self.lead_suit:
            return True
        return not any(c.suit == self.lead_suit for c in self.hand)


class MoveCheck:
    def __init__(self):
        self.checker = None
    
    def validate(self, card, hand, lead_suit):
        self.checker = CardChecker(hand, lead_suit)
        
        if card not in self.checker:
            if lead_suit:
                print(f"Must play {lead_suit} if you have it!")
            return False
        return True

move_check = MoveCheck()

def check_move(card_played, player_hand, first_suit, trump_suit):
    return move_check.validate(card_played, player_hand, first_suit)