import random

def create_deck():
    """Creates a standard 52-card deck and shuffles it."""
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    
    # Build the deck using nested loops
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
            
    random.shuffle(deck)
    return deck

def draw_cards(deck, count):
    """Removes a specific number of cards from the deck."""
    hand = []
    for _ in range(count):
        if len(deck) > 0:
            card = deck.pop()
            hand.append(card)
    return hand, deck

def show_card_visual(card):
    """Prints a visual ASCII representation of a playing card."""
    suit, rank = card
    # Adjust spacing for 10s so the borders don't break
    space = "" if rank == "10" else " "
    
    print(f"""
    +-------+

    |{rank}{space}     |
    |       |
    |   {suit}   |
    |       |
    |     {space}{rank}|
    +-------+
    """)

# --- Main Game Logic ---
def main():
    deck = create_deck()
    print("Welcome to the Python Card Drawer!")

    while len(deck) > 0:
        try:
            msg = f"How many cards do you want to draw? ({len(deck)} left): "
            num_cards = int(input(msg))
            
            if num_cards <= 0:
                print("Please enter a number greater than 0.")
                continue

            hand, deck = draw_cards(deck, num_cards)
            
            for card in hand:
                show_card_visual(card)
                
        except ValueError:
            print("Please enter a valid whole number.")

    print("We are out of cards! Thanks for playing.")

if __name__ == "__main__":
    main()

