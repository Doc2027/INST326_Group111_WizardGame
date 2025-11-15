def check_move(card_played, player_hand, first_suit, trump_suit):
    if card_played not in player_hand:
        print("You don't have that card!")
        return False
    
    if card_played == "Wizard" or card_played == "Jester":
        return True
    
    if first_suit == "":
        return True
    
    card_suit = get_card_suit(card_played)
    
    if card_suit == first_suit:
        return True
    
    has_led_suit = False
    for card in player_hand:
        if get_card_suit(card) == first_suit:
            has_led_suit = True
            break
    
    if has_led_suit:
        print(f"You must play a {first_suit} if you have one!")
        return False
    
    return True

def get_card_suit(card):
    if card == "Wizard" or card == "Jester":
        return "Special"
    
    parts = card.split("-")
    return parts[0]