import lesson1
from art import * #https://pypi.org/project/art/
import time as t
import sys
import cards
import practice
from sideKick import sideKick
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
          {LIGHT_GRAY}3: The Power of Bluffing & Deception
          {LIGHT_BLUE}4: Pot Odds & Equity{RESET}
          5: Reading Opponents & Adjusting Strategy
          {PURPLE}p: practice{RESET}
          {GREEN}sk: ANTEAI sidekick{RESET}
          {RED}q: Quit{RESET}
          """)
        choice = input(f"{BROWN}\nEnter a number 1-5 or {RED}q {BROWN}to quit{RESET}: ").lower()
        if choice.lower() == "q":
            print(f"{CYAN}Thanks for using AnteAI!{RESET} ",end="",flush=True)
            t.sleep(.5)
            for i in range(3):
                if i == 0:
                    print(f"{RED} Quitting", end="", flush=True)
                print(".", end="", flush=True)
                t.sleep(.5)
            sys.exit(0)
        elif choice == "p":
            practice.main(user_data)
        elif choice == "sk" or choice == "sidekick":
            sideKick(user_data["name"])
        elif choice == "1":
            tprint("LESSON 1")
            user_data = lesson1.start(user_data)
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
        else:
            print(f"{YELLOW}OOPS!{RESET} That's not a valid option.")
            card = cards.Card("2", "♦")
            print(card)



if __name__ == "__main__":
    main()