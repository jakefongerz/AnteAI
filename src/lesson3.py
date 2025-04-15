import time as t
import ante
# Resource:
# info for this lesson if from:
# https://upswingpoker.com/pot-odds-step-by-step/

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
RESET = "\033[0m"

def postLessonActivity(user_name):
    questions = [
        "When facing a bet on the turn with a flush draw, how do you decide whether to call based on pot odds? What specific numbers do you look at?",
        "If you expect your opponent to bet again on the river when you hit your draw, how do implied odds affect your decision on the turn?",
        "Imagine you have a draw and your pot odds suggest a call is barely profitable. What other factors might push you to fold instead?",
        "Can you think of a time when pot odds told you to call, but you lost anyway? What does that tell you about long-term thinking in poker?"
    ]
    print(f"You are crushing this lesson!")
    t.sleep(2)
    print(f"We have reached the end of this lesson. {CYAN}You can answer these questions in your own words{RESET}")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    for question in questions:
        ante.gaveQuestion(question)
        input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")



def implied_odds():
    print(f"\n{LIGHT_BLUE}Now that you understand {BOLD}pot odds{RESET}{LIGHT_BLUE}, let's introduce a related concept: {BOLD}implied odds.{RESET}")
    t.sleep(2)

    print("Implied odds are like pot odds, but with one important difference.")
    t.sleep(2)
    print(f"{YELLOW}They take into account the chips you expect to win {BOLD}after{RESET}{YELLOW} this round if you hit your draw.{RESET}")
    t.sleep(3)
    print("For example, let’s say the current pot is $50 and your opponent bets $10.")
    t.sleep(2)
    print("You’re being asked to call $10 to potentially win $60 total.")
    t.sleep(2)
    print("But... if you hit your hand, you think they’ll call an extra $30 on the next street.")
    t.sleep(2)
    print(f"{GREEN}So now, you’re not just trying to win $60—you’re estimating that you could win $90 total if things go your way.{RESET}")
    t.sleep(3)
    print("That extra $30 is what we call your 'implied odds.'")
    t.sleep(2)
    print("You're assuming you lose nothing more if you miss, but gain more if you hit.")
    t.sleep(2)
    print(f"{LIGHT_PURPLE}This concept helps you justify calls on draws that aren’t quite profitable using pot odds alone—but {BOLD}only{RESET}{LIGHT_PURPLE} if you’re confident you’ll get paid when you hit.{RESET}")
    t.sleep(3)
    input(f"{LIGHT_BLUE}Press Enter to continue...")
    #questions
    ask_mc_question(
    question="The pot is $40 and your opponent bets $10. You have a flush draw with one card to come. You believe if you hit your flush, you’ll win another $30 on the river. What are your implied pot odds?",
    options={
        "a": "5 to 1",
        "b": "3 to 1",
        "c": "7 to 1",
        "d": "None – you fold"
    },
    correct_option="c",
    explanation="If you call $10, the pot becomes $50. But with implied odds, you add the expected $30 on the river. That makes the implied pot $80. So, 80:10 = 8:1 (a small overestimate), but 7:1 is the closest correct choice."
)
    ask_mc_question(
    question="The pot is $60. Your opponent bets $20. You have an open-ended straight draw. If you hit, you expect to win an additional $40 on the next street. Should you call?",
    options={
        "a": "Yes, because implied odds justify it",
        "b": "No, because the pot odds are too low",
        "c": "Only if you're in late position",
        "d": "Call only if you have a pair"
    },
    correct_option="a",
    explanation="Pot odds = 80:20 → 4:1 = 20% equity needed. Add the implied $40 and pot becomes $120 → 120:20 = 6:1 = ~17% equity needed. Since your draw gives you about 32% equity, calling is profitable with implied odds."
)




def ask_mc_question(question, options, correct_option, explanation):
    print(f"\n{YELLOW}{question}{RESET}")
    for key, value in options.items():
        print(f"{key}. {value}")
    answer = input(f"{LIGHT_BLUE}Your answer (a/b/c/d): {RESET}").lower()
    
    if answer == correct_option:
        print(f"{GREEN}Correct!{RESET} {explanation}")
    else:
        print(f"{RED}Incorrect.{RESET} The correct answer was {correct_option}. {explanation}")
    t.sleep(2)


def using_pot_odds():
    print(f"Using Pot Odds")
    t.sleep(2)
    print(f"{LIGHT_BLUE}Let's walk through a real-world example of using {BOLD}pot odds{RESET}{LIGHT_BLUE} during a hand.{RESET}")
    t.sleep(2)

    print(f"\n{BOLD}Scenario:{RESET} Alice is holding {GREEN}5♣ 4♣{RESET}.")
    t.sleep(2)
    print("The board on the turn is: Q♣ J♣ 9♦ 7♥.")
    t.sleep(2)
    print("Alice has a flush draw—she needs one more club to complete it.")
    t.sleep(2)

    print(f"\n{YELLOW}How many outs does she have?{RESET}")
    t.sleep(1)
    print("There are 13 clubs total. 2 are in Alice's hand, and 2 are on the board.")
    t.sleep(1)
    print("That leaves {BOLD}9 remaining clubs{RESET}, or 9 outs.")
    t.sleep(2)

    print(f"\nThere are 52 cards in a deck.")
    print("Alice knows 6 of them (her 2 hole cards + 4 on the board).")
    print("So there are {BOLD}46 unknown cards left{RESET}.")
    t.sleep(2)
    print("Her chance of hitting a club on the river is 9 out of 46 — about {BOLD}19.6%{RESET}.")
    t.sleep(2)

    print(f"\nUsing the {CYAN}Rule of 2 and 4{RESET}, she multiplies her 9 outs by 2.")
    print("This gives an estimated {BOLD}18% equity{RESET}, which is close enough.")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...")
    # Pot odds breakdown
    print(f"\nNow let’s look at the pot:")
    t.sleep(1)
    print(f"\t{BOLD}- The current pot is $40{RESET}")
    t.sleep(1)
    print(f"\t{BOLD}- Her opponent bets $10, so the total pot is now $50{RESET}")
    t.sleep(1)
    print(f"\t{BOLD}- Alice has to call $10{RESET}")
    t.sleep(2)

    print(f"\nSo her pot odds are {BOLD}5 to 1 (50:10){RESET}")
    t.sleep(2)

    print(f"\nHer chance of completing her flush is {BOLD}4 to 1 against{RESET}.")
    t.sleep(2)
    print("Because her pot odds (5:1) are better than her draw odds (4:1),")
    t.sleep(2)
    print(f"{GREEN}Alice should make the call.{RESET}")
    t.sleep(3)
    input(f"{LIGHT_BLUE}Press Enter to continue...")
    # Discussion of assumptions
    print(f"\n{LIGHT_PURPLE}But wait! Let’s talk strategy...{RESET}")
    t.sleep(2)
    print("This decision assumes her opponent doesn't have a higher flush draw or a made hand.")
    t.sleep(2)
    print("If her opponent had A♣ K♣, for example, Alice would lose even if she hit her flush.")
    t.sleep(2)

    print("Pot odds are powerful, but they don’t replace thinking about your opponent’s possible range.")
    t.sleep(2)

    print(f"\n{CYAN}Pot odds are one part of a larger strategy that uses game theory{RESET}.")
    print("They help you make decisions based on math instead of guessing your opponent’s mood.")
    t.sleep(3)
    input(f"{LIGHT_BLUE}Press Enter to continue...")
    # Questions
    print(f"{CYAN}Let's test your understanding with a few questions:{RESET}")
    t.sleep(2)
    ask_mc_question(
    question="You hold 8♠ 7♠. The board on the turn is A♠ Q♠ 6♦ 2♥. Your opponent bets $20 into a $40 pot. Should you call?",
    options={
        "a": "Yes, pot odds are better than your odds of hitting",
        "b": "No, you don’t have enough equity to call",
        "c": "Yes, because you might have the best hand",
        "d": "Only if you're in late position"
    },
    correct_option="a",
    explanation="You have a flush draw with 9 outs → ~19.6% chance. Pot is $60 total, and it costs $20 to call → 3:1 pot odds = 25%. Since 25% > 19.6%, this is marginal but okay if you believe implied odds justify it."
)
    t.sleep(3)
    ask_mc_question(
    question="You have 5♣ 6♣. The board is K♣ 10♣ 9♦ 4♥. Your opponent bets $15 into a $45 pot. What are your pot odds, and should you call?",
    options={
        "a": "4 to 1; yes, call with strong pot odds",
        "b": "3 to 1; yes, call with close odds",
        "c": "4 to 1; no, your equity is too low",
        "d": "5 to 1; yes, but only if you’re in position"
    },
    correct_option="a",
    explanation="Pot is $60, and you must call $15 → 60:15 = 4:1 pot odds. Your flush draw gives you ~19.6% equity. Since 4:1 = 20%, your equity justifies calling."
)
    t.sleep(3)
    ask_mc_question(
    question="You hold 4♥ 3♥. The board is Q♥ 9♣ 2♥ 8♦. Your opponent bets $10 into a $30 pot. You have a flush draw. What else should you consider before calling?",
    options={
        "a": "You might hit a flush but still lose to a better one",
        "b": "The pot is too small to justify a call",
        "c": "You can’t make a straight or pair, so fold",
        "d": "The turn is too late to call a bet"
    },
    correct_option="a",
    explanation="You have a low flush draw. If your opponent has a higher heart draw (e.g. A♥ K♥), you could hit and still lose. This is where thinking about their range is critical."
)
    t.sleep(3)

def intro_pot_odds():
    print(f"{LIGHT_BLUE}Pot Odds{RESET}")
    t.sleep(2)
    print(f"{PURPLE}Pot odds{RESET} help you decide whether it's mathematically correct to call a bet.")
    t.sleep(2)
    print(f"Pot odds represent the {BROWN}ratio{RESET} between the size of the total pot and the size of the bet facing you.")
    t.sleep(2)
    print(" Keep in mind that the size of the total pot includes the bet(s) made in the current round.")
    t.sleep(2)
    print(f"{YELLOW}Pot odds = Total Pot Size : Call Amount{RESET}")
    t.sleep(2)
    print("\nLet’s look at an example:")
    t.sleep(1)
    print("There’s $2 in the pot, and your opponent bets $1.")
    t.sleep(2)
    print("Now the total pot is $3, and you have to call $1.")
    t.sleep(2)
    print(f"That means your pot odds are {GREEN}3 to 1 (3:1){RESET}.")
    t.sleep(2)
    print(f"\n{LIGHT_PURPLE}Now let’s walk through a full pot odds calculation step-by-step:{RESET}")
    t.sleep(2)

    # Step 1
    print(f"\n{BOLD}Step 1: Calculate the final pot size if you call.{RESET}")
    t.sleep(1)
    print("Example: Pot = $100, Opponent bets $50.")
    t.sleep(2)
    print(f"If you call, the final pot becomes {GREEN}$150 {CYAN}(existing pot){RESET} + {GREEN}$50 {CYAN}(your call){RESET} = {GREEN}$200{RESET}.")
    t.sleep(3)

    # Step 2
    print(f"\n{BOLD}Step 2: Divide your call by the final pot size.{RESET}")
    t.sleep(1)
    print("Call = $50, Final pot = $200.")
    t.sleep(2)
    print("50 / 200 = 0.25")
    t.sleep(2)

    # Step 3
    print(f"\n{BOLD}Step 3: Multiply by 100 to convert to a percentage.{RESET}")
    t.sleep(1)
    print("0.25 * 100 = 25%")
    t.sleep(2)
    print(f"{GREEN}This means your hand needs at least 25% equity to make a profitable call.{RESET}")
    t.sleep(3)

    print(f"\n{LIGHT_GREEN}That’s it! Pot odds show you how often your hand needs to win to break even.{RESET}")
    t.sleep(2)

    user_input = input(f"{LIGHT_BLUE}Would you like to try an example on your own? ({GREEN}y{RESET}/{RED}n{RESET}) ").lower()
    if user_input == "y":
        print("Awesome! Let's go over a few practice scenarios next.")
    else:
        print("No worries! We’ll keep moving forward when you’re ready.")
    # QUESTIONS
    ask_mc_question(
    question="The pot is $150. Your opponent bets $50. What percentage equity do you need to call profitably?",
    options={
        "a": "20%",
        "b": "25%",
        "c": "33%",
        "d": "40%"
    },
    correct_option="b",
    explanation="Final pot = $150 + $50 (opponent) + $50 (your call) = $250. 50 / 250 = 0.20 → 20% equity needed to call."
)

    ask_mc_question(
    question="The pot is $40 and your opponent goes all-in for $40. How often must you win to make a profitable call?",
    options={
        "a": "25%",
        "b": "33%",
        "c": "40%",
        "d": "50%"
    },
    correct_option="b",
    explanation="Final pot = $40 (pot) + $40 (opponent) + $40 (your call) = $120. 40 / 120 = 0.333 → 33%."
)
    ask_mc_question(
    question="The pot is $80. Your opponent bets $20. How often do you need to win to call profitably?",
    options={
        "a": "17%",
        "b": "25%",
        "c": "30%",
        "d": "33%"
    },
    correct_option="a",
    explanation="Final pot = $80 + $20 (opponent) + $20 (your call) = $120. 20 / 120 = 0.166 → ~17%"
)

def start(user_data):
    print(f"="*75)
    user_name = user_data.get("name")
    print(f"Heyyyy {user_name}! Let's learn about {BOLD}pot odds{RESET} and {BOLD}equity{RESET}.")
    t.sleep(2)
    print(f"{CYAN}By the end of this lesson you should have a good understanding of the following:")
    t.sleep(2)
    print(f"\t{PURPLE}Calculate Pot Odds Preflop{RESET}")
    t.sleep(2)
    print(f"\t{PURPLE}Calculate Pot Odds Postflop{RESET}")
    t.sleep(2)
    print(f"\t{PURPLE}Calculate Implied Odds{RESET}")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to get started...{RESET}")
    intro_pot_odds()
    using_pot_odds()
    implied_odds()
    postLessonActivity(user_name)
    user_data["lesson3"] = True
    return user_data    