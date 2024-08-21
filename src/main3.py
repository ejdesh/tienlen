import random

# Make a deck of cards
suits = ['S', 'C', 'D', 'H']  # Spades, Clubs, Diamonds, Hearts
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [rank + suit for suit in suits for rank in ranks]

def random_offset():
    return random.randint(-5, 5)

def split_deck():
    global deck
    half_deck_size = len(deck) // 2
    
    split_index = half_deck_size + random_offset()
    top_half, bottom_half = deck[:split_index], deck[split_index:]

    return top_half, bottom_half
    
def rifle_cards(split1, split2):
    global deck
    rifled_deck = []
    deck = [] # All the cards are in split1 and split2 now so we clear the deck

    while split1 or split2:
        if split1:
            deck.append(split1.pop())
        if split2:
            deck.append(split2.pop())

def cut_deck():
    global deck
    
    for _ in range(7): # Cut the deck 7 times for adequate randomness
        cut_index = 10 + random_offset()
        deck = deck[cut_index:] + deck[:cut_index]

def shuffle_deck():

    for i in range(0, 6):
        top_half, bottom_half = split_deck()
        rifle_cards(top_half, bottom_half)
        cut_deck()

def print_deck():
    print(deck)
    # TODO: print with pretty colors and symbols

def draw_2_of_hearts():
    red = "\033[91m"
    reset = "\033[0m"

    card = [
        "┌─────────┐",
        f"│2        │",
        f"│ {red}♥{reset}       │",
        "│         │",
        f"│    {red}♥{reset}    │",
        "│         │",
        f"│       {red}♥{reset} │",
        f"│        2│",
        "└─────────┘"
    ]

    for line in card:
        print(line)


def main():
    draw_2_of_hearts()
    shuffle_deck()
    print_deck()



main()
