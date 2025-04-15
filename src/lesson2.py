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
def postLessonActivity(user_name):
    questions = [
    "Why is it more acceptable to play weaker hands in late position?",
    "What types of hands do you think are safest to play from early position, and why?",
    "How does being suited or connected affect whether a hand is playable?",
    "When might it be a good idea to fold a hand like K-9 offsuit, even in late position?",
    "You have 4♦ 8♠ pre-flop. What should you do?",
    ]
    print(f"You are crushing this lesson!")
    t.sleep(2)
    print(f"I am going to give you a few questions to test your understanding of the lesson.    ")
    t.sleep(2)
    print(f"You can answer these questions in your own words")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    for question in questions:
        ante.gaveQuestion(question)
        input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")

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

def chart_based_strategy():
    print(f"Now that you know what position is, and why its important, you can use the chart below as a basic guide on {BOLD}which poker hands to play from which position.{RESET}")
    t.sleep(2)
    print("You only want to play a given hand if you are in the position to do so.")
    t.sleep(2)
    print(f"For the following charts, {GREEN}Any Position{RESET}, {BLUE}Mid or Late Position{RESET}, {YELLOW}Late Position{RESET}, {RED}Unplayable hand{RESET}")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    print(f"Pairs and Suited Hands{RESET}")
    print(f'''
{GREEN}A-A A-K K-Q Q-J J-T T-9 {BLUE}9-8 {YELLOW}8-7 7-6 6-5 5-4{RED} 4-3 3-2{RESET}
{GREEN}K-K A-Q K-J Q-T J-9 {BLUE}T-8{YELLOW} 9-7 8-6 7-5{RED} 6-4 5-3 4-2{RESET}
{GREEN}Q-Q A-J K-T {BLUE}Q-9 J-8 {YELLOW}T-7 9-6 {RED}8-5 7-4 6-3 5-2{RESET}
{GREEN}J-J A-T {BLUE}K-9 Q-8{YELLOW} J-7 T-6 {RED}9-5 8-4 7-3 6-2{RESET}
{GREEN}T-T {BLUE}A-9 {YELLOW}K-8 {RED}Q-7 J-6 T-5 9-4 8-3 7-2{RESET}
{GREEN}9-9{BLUE} A-8{YELLOW} K-7{RED} Q-6 J-5 T-4 9-3 8-2{RESET}
{GREEN}8-8{BLUE} A-7{YELLOW} K-6 {RED}Q-5 J-4 T-3 7-2{RESET}
{GREEN}7-7 {BLUE}A-6{YELLOW} K-5 {RED}Q-4 J-3 T-2{RESET}
{GREEN}{BLUE}6-6{YELLOW} A-5 K-4 {RED}Q-3 J-2{RESET}
{GREEN}{BLUE}5-5{YELLOW} A-4 K-3 {RED}Q-2{RESET}
{GREEN}{BLUE}{YELLOW}4-4 A-3 K-2{RESET}
{GREEN}{BLUE}{YELLOW}3-3 A-2{RESET}
{GREEN}{BLUE}{YELLOW}2-2{RESET}
          ''')
    print(f"Take some time and look over the chart. Memorize it. It will become second nature to you.")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    print(f"Offsuit Hands{RESET}")
    print(f'''
{GREEN}A-K K-Q {BLUE}Q-J J-T {YELLOW}T-9 9-8 8-7 {RED}7-6 6-5 5-4 4-3 3-2
{GREEN}A-Q K-J {BLUE}Q-T {YELLOW}J-9 T-8 9-7 {RED}8-6 7-5 6-4 5-3 4-2
{GREEN}A-J {BLUE}K-T {YELLOW}Q-9 J-8{RED} T-7 9-6 8-5 7-4 6-3 5-2
{GREEN}A-T {YELLOW}K-9 {RED}Q-8 J-7 T-6 9-5 8-4 7-3 6-2
{YELLOW}A-9 {RED}K-8 Q-7 J-6 T-5 9-4 8-3 7-2
{YELLOW}A-8{RED} K-7 Q-6 J-5 T-4 9-3 8-2
{YELLOW}A-7 {RED}K-6 Q-5 J-4 T-3 9-2
{RED}A-6 K-5 Q-4 J-3 T-2
{RED}A-5 K-4 Q-3 J-2
{RED}A-4 K-3 Q-2 J-2
{RED}A-3 K-2
{RED}A-2
          ''')

    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    print("remember this is only for pre-flop play. Post-flop you can make more informed decisions based on the board and other players' actions.")
    t.sleep(2)
    print(f"{LIGHT_BLUE}Let's talk about hand selection in {BOLD}late position{RESET}{LIGHT_BLUE}.{RESET}")
    t.sleep(2)
    print("In late position, players often open up their range of playable hands.")
    t.sleep(2)
    print("Why? Because if no one has entered the pot, even mediocre hands can be profitable.")
    t.sleep(2)
    print(f"{YELLOW}Stealing the blinds{RESET} with a raise is a great way to build your stack without needing a strong hand.")
    t.sleep(2)

    print("Most playable starting hands fall into a few key categories:")
    t.sleep(1)
    print(f"\t{GREEN}- Pairs{RESET}")
    t.sleep(1)
    print(f"\t{GREEN}- Aces (especially with decent kickers){RESET}")
    t.sleep(1)
    print(f"\t{GREEN}- Premium hands (like AK, AQ, KQ suited){RESET}")
    t.sleep(1)
    print(f"\t{GREEN}- Connectors (like 8♠ 9♠){RESET}")
    t.sleep(1)
    print(f"\t{GREEN}- One-gappers (like 7♣ 9♣){RESET}")
    t.sleep(3)

    print("Your position and the action before you help determine how wide you can open your range.")
    t.sleep(2)
    print(f"{LIGHT_GREEN}In late position, even hands that aren't traditionally strong can be playable.{RESET}")
    t.sleep(2)

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
    print(f"\t{GREEN}Make Informed Decisions Pre-Flop")
    t.sleep(1.5)
    input(f"{LIGHT_BLUE}Press Enter to begin...{RESET}")
    position_based_strategy(user_name)
    chart_based_strategy()
    postLessonActivity(user_name)
    user_data["lesson2"] = True
    return user_data