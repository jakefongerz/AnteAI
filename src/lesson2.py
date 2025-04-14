import time as t
import cards
import ante

# ANSI color codes
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

def position_based_strategy(user_name):
    print(f"{LIGHT_BLUE}Let's talk about your position at the poker table and why it matters!{RESET}")
    t.sleep(2)
    print(f"{YELLOW}Your position determines when it's your turn to act during a hand of poker.{RESET}")
    t.sleep(2)
    print(f"{GREEN}Players to the left of the dealer act first, and players to the right act last.{RESET}")
    t.sleep(2)
    print(f"{CYAN}The earlier your position, the stronger your starting hand needs to be.{RESET}")
    t.sleep(2)
    print("Why?")
    t.sleep(2)
    print(f"\tBecause more players are left to act after you—and any of them could have a better hand.")
    t.sleep(3)

    print(f"{LIGHT_PURPLE}Here is how positions are generally grouped at a 10-player table:{RESET}")
    t.sleep(2)

    print(f"{BOLD}- Early Position (EP):{RESET} {GREEN}UTG1, UTG2, UTG3 (Under the Gun){RESET}")
    t.sleep(2)
    print(f"{BOLD}- Middle Position (MP):{RESET} MP1, MP2, MP3")
    t.sleep(2)
    print(f"{BOLD}- Late Position (LP):{RESET} Highjack (HJ), Cutoff (CO), Button (BU)")
    t.sleep(2)
    print(f"{BOLD}- Blinds:{RESET} Small Blind (SB), Big Blind (BB)")
    t.sleep(4)

    print(f"{YELLOW}Late position is the most powerful—it gives you more information before you act!{RESET}")
    t.sleep(2)

    print(f"{LIGHT_RED}What if there are fewer than 10 players at the table?{RESET}")
    t.sleep(2)
    print("You start removing seats from early positions first, then middle, and so on.")
    t.sleep(2)

    user_input = input(f"{LIGHT_BLUE}Does the idea of table position make sense? ({GREEN}y{RESET}/{RED}n{RESET}) ").lower()
    if user_input == "y":
        print("Awesome! Let's keep going.")
    else:
        question = input(f"{LIGHT_BLUE}What part about position would you like explained again?{RESET} ")
        ante.askQuestion([f"User ({user_name}) is confused about table position and asks: {question}"])
        input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")



def start(user_data):
    user_name = user_data.get("name")
    print(f"="*50)
    t.sleep(1)
    print(f"{GREEN}Hey {user_name}! Welcome to Lesson 2!")
    t.sleep(2)
    # Lesson 2 objectives:
    print(f"{CYAN}By the end of this lesson you should have a good understanding of the following:")
    t.sleep(1.5)
    print(f"\t{PURPLE}Identify Strong Starting Hands{RESET}")
    t.sleep(1.5)
    print(f"\t{RED}Apply Position-Based Strategy")
    t.sleep(1.5)
    print(f"\t{BLUE}Distinguish Between Tight and Loose Playstyles")
    t.sleep(1.5)
    print(f"\t{GREEN}Make Informed Decisions Pre-Flop")
    t.sleep(1.5)
    input(f"{LIGHT_BLUE}Press Enter to begin...{RESET}")
