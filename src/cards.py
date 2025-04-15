BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
RESET = "\033[0m"

def get_card(rank, suit):
    if suit == "♥" or suit == "♦":
        rank = f"{RED}{rank} {RESET}"
        suit = f"{RED}{suit}{RESET}"
    card =  f"""
┌─────────┐
│ {rank:<2}      │
│         │
│    {suit}    │
│         │
│      {rank:>2} │
└─────────┘
"""
    return card

def get_hole_cards(rank1, suit1, rank2, suit2):
    if suit1 == "♥" or suit1 == "♦":
        rank1 = f"{RED}{rank1} {RESET}"
        suit1 = f"{RED}{suit1}{RESET}"
    if suit2 == "♥" or suit2 == "♦":
        rank2 = f"{RED}{rank2} {RESET}"
        suit2 = f"{RED}{suit2}{RESET}"
    cards = f"""
┌─────────┐ ┌─────────┐
│ {rank1:<2}      │ │ {rank2:<2}      │
│         │ │         │
│    {suit1}    │ │    {suit2}    │
│         │ │         │
│      {rank1:>2} │ │      {rank2:>2} │
└─────────┘ └─────────┘
"""
    return cards

def get_cards_on_table(cards):
    # cards is a list of lists, each inner list contains a rank and a suit
    if cards[0][1] == "♥" or cards[0][1] == "♦":
        cards[0][0] = f"{RED}{cards[0][0]} {RESET}"
        cards[0][1] = f"{RED}{cards[0][1]}{RESET}"
    if cards[1][1] == "♥" or cards[1][1] == "♦":
        cards[1][0] = f"{RED}{cards[1][0]} {RESET}"
        cards[1][1] = f"{RED}{cards[1][1]}{RESET}"
    if cards[2][1] == "♥" or cards[2][1] == "♦":
        cards[2][0] = f"{RED}{cards[2][0]} {RESET}"
        cards[2][1] = f"{RED}{cards[2][1]}{RESET}"
    if cards[3][1] == "♥" or cards[3][1] == "♦":
        cards[3][0] = f"{RED}{cards[3][0]} {RESET}"
        cards[3][1] = f"{RED}{cards[3][1]}{RESET}"
    if cards[4][1] == "♥" or cards[4][1] == "♦":
        cards[4][0] = f"{RED}{cards[4][0]} {RESET}"
        cards[4][1] = f"{RED}{cards[4][1]}{RESET}"
    cards_on_table = f"""
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ {cards[0][0]:<2}      │ │ {cards[1][0]:<2}      │ │ {cards[2][0]:<2}      │ │ {cards[3][0]:<2}      │ │ {cards[4][0]:<2}      │
│         │ │         │ │         │ │         │ │         │
│    {cards[0][1]}    │ │    {cards[1][1]}    │ │    {cards[2][1]}    │ │    {cards[3][1]}    │ │    {cards[4][1]}    │
│         │ │         │ │         │ │         │ │         │
│      {cards[0][0]:>2} │ │      {cards[1][0]:>2} │ │      {cards[2][0]:>2} │ │      {cards[3][0]:>2} │ │      {cards[4][0]:>2} │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
"""
    return cards_on_table

# Example: Printing a hand of cards
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['♠', '♣', '♥', '♦']
cards = [get_card(rank, suit) for rank, suit in zip(ranks, suits)]
#print(get_card("2", "♦"))
##print(get_hole_cards("2", "♦", "3", "♣"))
#print(get_cards_on_table([["5", "♦"], ["3", "♣"], ["4", "♥"], ["5", "♠"], ["6", "♣"]]))
