import lesson1
from art import * #https://pypi.org/project/art/
import time as t
import sys

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


def main():
    tprint("ANTE AI")
    print("-"*50)
    t.sleep(.5)
    print(f"{YELLOW}Hey there!{RESET}")
    t.sleep(.75)
    print(f"{PURPLE}I'm AnteAI, your AI poker tutor.{RESET}")
    t.sleep(1)
    user_name = input(f"{BROWN}What's your name? {RESET}")
    if user_name == "":
        user_name = f"{LIGHT_CYAN}Dude{RESET}"
        print(f"I'll just call you {BOLD}Dude{RESET} then.")
    else:
        user_name = f"{LIGHT_CYAN}{user_name}{RESET}"
        print(f"Nice to meet you {user_name}! ")
        t.sleep(1)
        print(f"Let's get started!")
    user_data = {"name": user_name, "lesson1": False, "lesson2": False, "lesson3": False, "lesson4": False, "lesson5": False, "lesson6": False, "lesson7": False, "lesson8": False, "lesson9": False, "lesson10": False}
    t.sleep(1)
    menu(user_data)

def menu(user_data):
    print(f"Choose a lesson to start with... {RESET}")
    t.sleep(1)
    while True:
        print(f"""\t  {YELLOW}1: Poker Basics & Rules{RESET}
          2: Starting Hand Selection
          {CYAN}3: Positional Awareness & Betting Rounds{RESET}
          4: The Power of Bluffing & Deception
          {LIGHT_BLUE}5: Pot Odds & Equity{RESET}
          6: Continuation Betting & Aggressive Play
          {LIGHT_GRAY}7: Reading Opponents & Adjusting Strategy{RESET}
          8: Advanced Postflop Play
          {PURPLE}9: Bankroll Management & Mindset{RESET}
          10: Tournament vs. Cash Game Strategy
          {RED}q: Quit{RESET}
          """)
        choice = input(f"{BROWN}\nEnter a number 1-10 or {RED}q {BROWN}to quit{RESET}: ").lower()
        if choice.lower() == "q":
            print(f"{CYAN}Thanks for using AnteAI!{RESET}")
            t.sleep(1)
            sys.exit()
        elif choice == "1":
            tprint("LESSON 1")
            lesson1.start(user_data.get("name"))
        elif choice == "2":
            tprint("LESSON 2")
            print("Lesson 2")
        elif choice == "3":
            tprint("LESSON 3")
            print("Lesson 3")
        elif choice == "4":
            tprint("LESSON 4")
            print("Lesson 4")
        elif choice == "5":
            tprint("LESSON 5")
            print("Lesson 5")
        elif choice == "6":
            tprint("LESSON 6")
            print("Lesson 6")
        elif choice == "7":
            tprint("LESSON 7")
            print("Lesson 7")
        elif choice == "8":
            tprint("LESSON 8")
            print("Lesson 8")
        elif choice == "9":
            tprint("LESSON 9")
            print("Lesson 9")
        elif choice == "10":
            tprint("LESSON 10")
            print("Lesson 10")
        else:
            print(f"{YELLOW}OOPS!{RESET} That's not a valid option.")



if __name__ == "__main__":
    main()