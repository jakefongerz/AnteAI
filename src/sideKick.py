import time as t
import ante

LIGHT_BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

def sideKick(user_name):
    print("Welcome to the sidekick section!")
    t.sleep(2)
    first_time = True
    while True:
        if first_time:
            user_input = input(f"{LIGHT_BLUE}What can I help you with?{RESET}")
            first_time = False
        else:
            user_input = input(f"{LIGHT_BLUE}What else can I help you with? ({RED}q{RESET} to quit){RESET}")
            if user_input.lower() == "q" or user_input.lower() == "quit":
                break
        ante.askQuestion(f"User ({user_name}) is asking you the following question: {user_input}")
    print("Thanks for using AnteAI's sidekick!")
    t.sleep(2)
    print("Returning to main menu...")
    t.sleep(1)


