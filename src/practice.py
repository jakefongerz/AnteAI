import time as t
import cards
import ante
#  ANSI color codes
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


poker_table = f"""

                     BU   SB   BB     
                +----------------------+  
            CO  |                      |  UTG1
                |      POKER TABLE     |  
            HJ  |                      |  UTG2
                +----------------------+  
                    MP3   MP2   MP1

                   Dealer is at the Button (BU)
"""

# ['♠', '♣', '♥', '♦']
scenerios = {
    "2": {
        "user_position": "UTG1",
        "user_cards": [["J", "♦"], [ "5", "♠"]],
        "pot": 20,
        "cards_on_table": [["K", "♦"], ["8", "♣"], ["5", "♥"], [" ", " "], [" ", " "]],
        "description": f'''
        The {PURPLE}HJ{RESET}, usually aggressive, has only checked so far—unusual behavior that may signal weakness or a trap. 
        {PURPLE}MP1{RESET}, who typically folds early, stayed in the hand, suggesting possible strength. 
        The {PURPLE}CO{RESET} and {PURPLE}BU{RESET} have been passive, and the blinds have not shown interest postflop. 
        Action has been cautious, and you are first to act from {PURPLE}UTG1{RESET}.''',
        "question": f" {BOLD}What should you do next? What should you watch out for? {GREEN}(explain your reasoning){RESET}"
    },
    "1": {
        "user_position": "CO",
        "user_cards": [["A", "♠"], ["9", "♠"]],
        "pot": 36,
        "cards_on_table": [["J", "♠"], ["6", "♠"], ["2", "♦"], [" ", " "], [" ", " "]],
        "description": f'''{PURPLE}BU{RESET} raised preflop, and you called in position. 
        {PURPLE}SB{RESET} and {PURPLE}BB{RESET} both folded. 
        On the flop, {PURPLE}BU{RESET} continuation bet about half the pot.''',
        "question": f" {BOLD}You have the nut flush draw and overcard. Do you call, raise to apply pressure, or fold if you think {PURPLE}BU{RESET} has a strong made hand? {GREEN}(explain your reasoning){RESET}"  
},     
    "9": {
        "user_position": "MP2",
        "user_cards": [["Q", "♣"], ["5", "♥"]],
        "pot": 48,
        "cards_on_table": [["Q", "♦"], ["9", "♠"], ["4", "♣"], [" ", " "], [" ", " "]],
        "description": f'''{PURPLE}UTG2{RESET} limped in, and {PURPLE}MP1{RESET} raised 3x BB preflop. 
        You called, and both {PURPLE}CO{RESET} and {PURPLE}BB{RESET} came along. On the flop, {PURPLE}MP1{RESET} c-bet half pot, and only you and {PURPLE}BB{RESET} called.
        The {PURPLE}BB{RESET} is known to float with backdoor draws.''',
        "question": f" {BOLD}Should you raise to protect your top pair or just call? What does {PURPLE}MP1{RESET}’s line tell you? {GREEN}(explain your reasoning){RESET}"
    },
    "4": {
        "user_position": "BU",
        "user_cards": [["8", "♦"], ["8", "♣"]],
        "pot": 30,
        "cards_on_table": [["Q", "♥"], ["3", "♦"], ["6", "♠"], [" ", " "], [" ", " "]],
        "description": f'''{PURPLE}MP3{RESET} limped and SB called.
    You raised on the Button, and both players called.
    On the flop,{PURPLE} MP3{RESET} checked, and SB made a small lead bet.
    {PURPLE}MP3{RESET} flatted again. Both players are known to play passively unless they hit big.''',
        "question": f" {BOLD}Do you raise for value or pot control with a mid pair? What are the risks of just calling? {GREEN}(explain your reasoning){RESET}"
    },
    "5": {
        "user_position": "SB",
        "user_cards": [["K", "♥"], ["J", "♥"]],
        "pot": 60,
        "cards_on_table": [["J", "♦"], ["8", "♣"], ["3", "♠"], [" ", " "], [" ", " "]],
        "description": f'''Four players saw the flop. {PURPLE}UTG{RESET} called, and {PURPLE}CO{RESET} folded. Action is back on you.
    You checked, {PURPLE}BB{RESET} bet small, {PURPLE}UTG{RESET} called, and {PURPLE}CO{RESET} folded. 
    Action is back on you.''',
        "question": f"{BOLD}You hit top pair with a decent kicker. Do you raise to isolate, call to control the pot, or fold if you fear slow-played monsters? {GREEN}(explain your reasoning){RESET}"
    },
    "6": {
        "user_position": "MP2",
        "user_cards": [["7", "♥"], ["6", "♥"]],
        "pot": 80,
        "cards_on_table": [["A", "♣"], ["9", "♥"], ["2", "♥"], ["K", "♦"], [" ", " "]],
        "description": f'''{PURPLE}UTG{RESET} raised preflop and has been aggressive on both the flop and turn. 
        They just bet $40 into a pot of $80. 
        You have a flush draw with one card to come. {PURPLE}UTG{RESET} is a tight player who rarely bluffs.''',
        "question": f"{BOLD}Based on pot odds, is it profitable to call? How might implied odds or their tight image affect your decision? {GREEN}(explain your reasoning){RESET}"
    },
        "7": {
        "user_position": "CO",
        "user_cards": [["5", "♣"], ["4", "♣"]],
        "pot": 60,
        "cards_on_table": [["K", "♣"], ["Q", "♠"], ["7", "♣"], ["2", "♦"], [" ", " "]],
        "description": "BTN raised preflop and has been playing aggressively. On the turn, they bet $20 into the $60 pot. They often barrel river bets. You have a flush draw and position.",
        "question": "What are your pot odds here, and how do implied odds make calling more or less attractive?"
    },
    "8": {
        "user_position": "BU",
        "user_cards": [["A", "♦"], ["9", "♠"]],
        "pot": 72,
        "cards_on_table": [["6", "♣"], ["7", "♦"], ["3", "♥"], ["Q", "♠"], [" ", " "]],
        "description": f'''{PURPLE}CO{RESET} raised preflop and c-bet the flop. 
        You called on the button with just ace-high, hoping to pick up the pot later. 
        On the turn, {PURPLE}CO{RESET} checks to you. 
        They tend to slow down without strong holdings. 
        Everyone else has folded.''',
        "question": f"{BOLD}Should you check behind and take a free river, or bluff to represent a queen? How does your position and their check influence your move? {GREEN}(explain your reasoning){RESET}"
    },
    "3": {
        "user_position": "MP1",
        "user_cards": [["8", "♦"], ["8", "♣"]],
        "pot": 100,
        "cards_on_table": [["J", "♠"], ["9", "♣"], ["7", "♣"], [" ", " "], [" ", " "]],
        "description": f'''{PURPLE}UTG{RESET} player raised preflop and you called with a pocket pair. 
        On the flop, {PURPLE}UTG{RESET} bets $30 into the $100 pot. 
        The board is highly connected and draws are possible. 
        {PURPLE}UTG{RESET} is known to continuation bet with both made hands and overcards.''',
        "question": f"{BOLD}You have middle pair on a dangerous board. Do you call, raise to protect, or fold? How do pot odds and board texture guide your thinking? {GREEN}(explain your reasoning){RESET}"
    }
}



def run_scenerio(scenerio):
    print(f"Hey! Let's play a game of poker!")
    t.sleep(2)
    print(f"You are at the {scenerio['user_position']} position.")
    t.sleep(2)
    print(f"{CYAN}{poker_table}{RESET}")
    t.sleep(2)
    print(f"Your cards are:")
    t.sleep(2)
    hole_cards = cards.get_hole_cards(scenerio['user_cards'][0][0], scenerio['user_cards'][0][1], scenerio['user_cards'][1][0], scenerio['user_cards'][1][1])
    print(hole_cards)
    t.sleep(2)
    print(f"The cards on the table are:")
    t.sleep(2)
    table_cards = cards.get_cards_on_table(scenerio['cards_on_table'])
    print(table_cards)
    t.sleep(2)
    print(f"The pot is currently set at{GREEN} {scenerio['pot']}{RESET}.")
    t.sleep(2)
    ante.slow_print(f"{scenerio['description']}")
    t.sleep(2)
    print(f"Answer the following questions below in a signal response")
    user_response = input(f"{scenerio['question']}")
    print(" ")
    ante.askQuestion(f"The user was given the following scenerio: {scenerio} The user's response was: {user_response}")


def main(user_data):
    print("Welcome to the practice section!")
    t.sleep(1)
    print("You can practice your poker skills here.")
    input(f"{LIGHT_BLUE}Press Enter to get started...{RESET}")
    for i in range(1,6):
        print(f"Scenerio {i}")
        run_scenerio(scenerios[f"{i}"])
        t.sleep(1)
        print("Ready for the next scenerio?")
        user_input = input(f"{LIGHT_BLUE}Press Enter to continue or {RED}q{RESET} to quit...{RESET}").lower()
        if user_input == "q" or user_input == "quit":
            break
    print("Thanks for practicing!")
    t.sleep(1)
    print("Quitting practice section...")
    t.sleep(1)


