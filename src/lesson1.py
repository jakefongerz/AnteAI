import time as t
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

# https://pokerpower.com/how-to-play-texas-hold-em/

def card_refresher(user_name):
    print("="*50)
    print("STANDARD DECK OF CARDS")
    t.sleep(2)
    print("Poker is a card game that is played with a deck of 52 cards.")
    t.sleep(3)
    print(f"The deck of cards has 4 suits: {RED} hearts \u2665, diamonds \u2666, {RESET}clubs \u2663, and spades \u2660.")
    t.sleep(3)
    print("Each suit has 13 cards: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.")
    t.sleep(3)
    hasQuestion = input(f"{LIGHT_BLUE}Do you have any questions so far? ({GREEN}y{RESET}/{RED}n{RESET})").lower()
    t.sleep(1)
    if hasQuestion == "y":
        question = input("What is your question?")
        ante.askQuestion([f"User ({user_name}) just learned that a standard deck of cards has 4 suits and 13 cards (and what they are) they are asking you the following question: {question}"])
        input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    else:
        print("Let's continue!")
    user_response = input(f"{LIGHT_BLUE}Knowledge check:{RESET} How many aces are in a standard deck of cards? (1/2/3/4) ").lower()
    t.sleep(1)
    if user_response == "4" or user_response == "four":
        print(f"{GREEN}Correct! There are 4 of each card in a standard deck of cards.{RESET}")
    else:
        print(f"{RED}Incorrect! There are 4 of each card in a standard deck of cards.{RESET}")
    t.sleep(1)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")

def poker_hand_questions(user_name):
    print(f"{BLUE}That was a lot of information to take in!")
    t.sleep(1)
    print(f"{PURPLE}Let's test your knowledge of poker hands! Answer the following questions:{RESET}")
    t.sleep(2)

    # Question 1
    q1 = input(f"{YELLOW}1. Which hand is stronger? {GREEN}A Full House{RESET} or {BLUE}Four of a Kind{RESET}? ").lower()
    if "four" in q1 or "4" in q1:
        print(f"{GREEN}Correct! Four of a Kind beats a Full House.{RESET}")
    else:
        print(f"{RED}Incorrect! Four of a Kind is stronger than a Full House.{RESET}")
    t.sleep(2)

    # Question 2
    q2 = input(f"{YELLOW}2. What is the highest possible hand in poker?{RESET} ").lower()
    if "royal flush" in q2:
        print(f"{GREEN}Correct! A Royal Flush is the strongest hand in poker.{RESET}")
    else:
        print(f"{RED}Incorrect! The highest hand is a Royal Flush.{RESET}")
    t.sleep(2)

    # Question 3
    q3 = input(f"{YELLOW}3. Which hand consists of five consecutive cards of different suits?{RESET} ").lower()
    if "straight" in q3:
        print(f"{GREEN}Correct! A Straight is five consecutive cards in different suits.{RESET}")
    else:
        print(f"{RED}Incorrect! The correct answer is a Straight.{RESET}")
    t.sleep(2)

    # Question 4
    q4 = input(f"{YELLOW}4. If two players both have a Flush, how do you determine the winner?{RESET} ").lower()
    if "highest card" in q4 or "kicker" in q4 or "high card" in q4:
        print(f"{GREEN}Correct! The player with the highest card in their Flush wins.{RESET}")
    else:
        print(f"{RED}Incorrect! The winner is determined by the highest card in the Flush.{RESET}")
    t.sleep(2)

    # Question 5
    q5 = input(f"{YELLOW}5. Which hand is stronger? {GREEN}A Straight{RESET} or {CYAN}A Flush{RESET}? ").lower()
    if "flush" in q5:
        print(f"{GREEN}Correct! A Flush is stronger than a Straight.{RESET}")
    else:
        print(f"{RED}Incorrect! A Flush beats a Straight.{RESET}")
    t.sleep(2)

    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")


def hand_rankings(user_name):
    print("The poker hand is a combination of 5 cards.")
    t.sleep(2)
    print(f"The poker hand is ranked from high to low:{YELLOW} Royal Flush, {GREEN}Straight Flush, {BLUE}Four of a Kind, {PURPLE}Full House, {CYAN}Flush, {LIGHT_GREEN}Straight, {LIGHT_BLUE}Three of a Kind, {LIGHT_PURPLE}Two Pair, {LIGHT_RED}One Pair, {RED}High Card.{RESET}")
    t.sleep(3)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    print(f"{YELLOW}Royal Flush{RESET} is the {BOLD}highest{RESET} hand in poker.")
    t.sleep(2)
    print(f"A Royal Flush is a straight from a ten to an ace and all five cards are of the same suit")
    t.sleep(2)
    print(f"{GREEN}Straight Flush{RESET} is the second strongest hand in poker.")
    t.sleep(2)
    print(f"A Straight Flush is any five consecutive cards of the same suit (e.g., 5-6-7-8-9 of hearts).")
    t.sleep(2)
    print(f"{BLUE}Four of a Kind{RESET}, also known as 'Quads,' is the third strongest hand.")
    t.sleep(2)
    print(f"This hand consists of four cards of the same rank (e.g., 9-9-9-9-K).")
    t.sleep(2)
    print(f"{PURPLE}Full House{RESET} is a combination of a Three of a Kind and a Pair.")
    t.sleep(2)
    print(f"For example, having three Queens and two Fives (Q-Q-Q-5-5) makes a Full House.")
    t.sleep(2)
    print(f"{CYAN}Flush{RESET} is a hand where all five cards are of the same suit, but not in sequence.")
    t.sleep(2)
    print(f"For example, A-10-7-4-2, all in spades, would be a Flush.")
    t.sleep(2)
    print(f"{LIGHT_GREEN}Straight{RESET} consists of five consecutive cards in mixed suits.")
    t.sleep(2)
    print(f"For example, 6-7-8-9-10 of different suits forms a Straight.")
    t.sleep(2)
    print(f"{LIGHT_BLUE}Three of a Kind{RESET} is a hand with three cards of the same rank.")
    t.sleep(2)
    print(f"For example, J-J-J-8-2 would be a Three of a Kind.")
    t.sleep(2)
    print(f"{LIGHT_PURPLE}Two Pair{RESET} is exactly what it sounds like—a hand with two different pairs.")
    t.sleep(2)
    print(f"For example, K-K-7-7-4 would be a Two Pair.")
    t.sleep(2)
    print(f"{LIGHT_RED}One Pair{RESET} is a hand that contains just one pair of matching cards.")
    t.sleep(2)
    print(f"For example, A-A-9-6-3 would be a One Pair hand.")
    t.sleep(2)
    print(f"{RED}High Card{RESET} is the lowest possible hand in poker.")
    t.sleep(2)
    print(f"If no one has at least a pair, the player with the highest card wins (e.g., A-K-10-7-4, where Ace is the highest card).")
    t.sleep(2)
    print("These are the possibilities for poker hands.")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    t.sleep(2)
    print("Any hand of a certain category is stronger than any hand in a lower category.") 
    t.sleep(2)
    print("For example, any full house beats any straight.")
    t.sleep(2)
    print(f"If two players have the {LIGHT_BLUE} same category of hand {RESET}, the winner is whoever uses the {LIGHT_BLUE} highest cards {RESET}(ace is the highest, 2 is the lowest.)")
    t.sleep(2)
    print(f"If players have the {LIGHT_BLUE} exact same five-card hand {RESET}, they evenly {LIGHT_GREEN} split the chips in the middle.")
    t.sleep(2)
    
    user_input = input(f"{LIGHT_BLUE}Does that make sense? ({GREEN}y{RESET}/{RED}n{RESET}) ").lower()
    if user_input.contains("y"):
        print("Awesome! Now, let's dive into how betting works.")
    else:
        question = input(f"{LIGHT_BLUE}No problem! What are you confused about?{RESET} ")
        ante.askQuestion([f"User ({user_name}) is confused about poker hand rankings and asks: {question}"])
        input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")


def objectives_of_poker(user_name):
    print(f"The most popular form of poker is {LIGHT_CYAN}{BOLD}Texas Hold em{RESET} and so we will focus on that.")
    t.sleep(2)
    print(f"{RED}The goal in any poker game is to win all the chips")
    t.sleep(2)
    print(f"{LIGHT_RED}Chips are tokens used in poker to represent {GREEN}money{LIGHT_RED} or {GREEN}stakes.")
    t.sleep(2)
    print(f"{YELLOW}There are two ways to win chips")
    t.sleep(2)
    print(f"\t {GREEN}1. By having the best hand when it is time to show your cards.")
    t.sleep(2)
    print(f"\t 2. By getting your opponents to fold before they are able to show their cards.{RESET}")
    t.sleep(2)
    print(f"Players make their {BOLD}five-card hands{RESET} by using their two hole cards and the five community cards.")
    t.sleep(2)
    user_input = input(f"{LIGHT_BLUE}Does that make sense? ({GREEN}y{RESET}/{RED}n{RESET})").lower()
    t.sleep(1)
    if user_input == "y":
        print("Great, let us continue!")
    else:
        question = input(f"{LIGHT_BLUE}No Worries, what are you confused about?{RESET} ")
        ante.askQuestion([f"User ({user_name}) is confused about the basic goals of poker and asks you the following question: {question}"])
        input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")


def structure_of_texas_hold_em(user_name):
    print(f"{YELLOW}The game follows a set flow with four main betting rounds:{RESET}")
    t.sleep(2)
    print(f"\t{GREEN}1. Pre-Flop{RESET} - Players receive their hole cards and place initial bets.")
    t.sleep(1)
    print(f"\t{GREEN}2. Flop{RESET} - Three community cards are dealt face-up.")
    t.sleep(1)
    print(f"\t{GREEN}3. Turn{RESET} - A fourth community card is dealt.")
    t.sleep(1)
    print(f"\t{GREEN}4. River{RESET} - The fifth and final community card is dealt.")
    t.sleep(2)

    print(f"{LIGHT_RED}Before the cards are dealt, two players must post blinds:{RESET}")
    t.sleep(2)
    print(f"\t{LIGHT_PURPLE}- {GREEN}Small Blind{RESET}: The player to the left of the dealer posts a small forced bet.")
    t.sleep(1)
    print(f"\t{LIGHT_PURPLE}- {GREEN}Big Blind{RESET}: The next player posts a bet that is usually double the small blind.")
    t.sleep(2)
    print(f"{CYAN}These forced bets create action and ensure there are chips to play for!{RESET}")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    # Pre-Flop
    print(f"\n{YELLOW}Pre-Flop:{RESET} The first betting round begins!")
    t.sleep(2)
    print(f"Each player is dealt {BOLD}two hole cards{RESET} that only they can see.")
    t.sleep(2)
    print(f"The player to the left of the big blind takes the first action.")
    t.sleep(2)
    print(f"They can:")
    t.sleep(2)
    print(f"\t{GREEN}- Call{RESET}: Match the big blind amount.")
    t.sleep(2)
    print(f"\t{RED}- Fold{RESET}: Discard their cards and sit out this hand.")
    t.sleep(2)
    print(f"\t{LIGHT_GREEN}- Raise{RESET}: Increase the bet, making it more expensive for others to continue.")
    t.sleep(3)

    print(f"The action continues clockwise around the table until all bets are matched or only one player remains.")
    t.sleep(2)
    print(f"If everyone but one player folds, that player wins the pot immediately!")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    # Flop
    print(f"\n{YELLOW}Flop:{RESET} Three community cards are dealt face-up.")
    t.sleep(2)
    print(f"These cards are shared by all players to help make the best five-card hand.")
    t.sleep(2)
    print(f"The first remaining player to the left of the dealer now decides:")
    t.sleep(2)
    print(f"\t{LIGHT_GREEN}- Check{RESET}: Pass the action to the next player without betting.")
    t.sleep(2)
    print(f"\t{GREEN}- Bet{RESET}: Place a wager to stay in the hand.")
    t.sleep(2)
    print(f"\t{RED}- Fold{RESET}: If a bet is made, a player may fold instead of calling.")
    t.sleep(3)

    print(f"If a bet is placed, players can call, raise, or fold, just like in the Pre-Flop round.")
    t.sleep(2)
    print(f"If all players check or match the last bet, we move to the next round!")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    # Turn
    print(f"\n{YELLOW}Turn:{RESET} A fourth community card is dealt face-up.")
    t.sleep(2)
    print(f"The betting process repeats just like on the flop.")
    t.sleep(2)
    print(f"Players still in the hand decide whether to check, bet, call, raise, or fold.")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    # River
    print(f"\n{YELLOW}River:{RESET} The fifth and final community card is dealt.")
    t.sleep(2)
    print(f"This is the last chance for players to bet or bluff before the showdown!")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    # Showdown
    print(f"\n{YELLOW}Showdown:{RESET} If multiple players are still in the hand, they reveal their cards.")
    t.sleep(2)
    print(f"The player with the {BOLD}best five-card hand{RESET} using their two hole cards and the five community cards wins the pot!")
    t.sleep(2)
    print(f"If there's a tie, the pot is split among the winners.")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")
    print(f"{LIGHT_GREEN}And that's a complete hand of Texas Hold'em!{RESET}")
    t.sleep(2)

    user_input = input(f"{LIGHT_BLUE}Does that game flow make sense? ({GREEN}y{RESET}/{RED}n{RESET}) ").lower()
    if user_input == "y":
        print("Awesome! You're ready to learn about poker strategy next.")
    else:
        question = input(f"{LIGHT_BLUE}No problem! What part are you confused about?{RESET} ")
        ante.askQuestion([f"User ({user_name}) is confused about Texas Hold'em game flow and asks: {question}"])
        input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")

def game_flow_questions(user_name):
    print(f"{LIGHT_BLUE}Let's see how well you understand the flow of a Texas Hold'em hand!{RESET}")
    t.sleep(2)

    # Question 1
    q1 = input(f"{YELLOW}1. What are the four main betting rounds in Texas Hold'em?{RESET} ").lower()
    if all(word in q1 for word in ["pre-flop", "flop", "turn", "river"]):
        print(f"{GREEN}Correct! The four betting rounds are Pre-Flop, Flop, Turn, and River.{RESET}")
    else:
        print(f"{RED}Incorrect! The correct answer is Pre-Flop, Flop, Turn, and River.{RESET}")
    t.sleep(2)

    # Question 2
    q2 = input(f"{YELLOW}2. Who posts the blinds before a hand begins?{RESET} ").lower()
    if "small blind" in q2 and "big blind" in q2:
        print(f"{GREEN}Correct! The player to the left of the dealer posts the Small Blind, and the next player posts the Big Blind.{RESET}")
    else:
        print(f"{RED}Incorrect! The correct answer is the Small Blind and Big Blind, posted by the two players to the left of the dealer.{RESET}")
    t.sleep(2)

    # Question 3
    q3 = input(f"{YELLOW}3. What happens if all players except one fold during any betting round?{RESET} ").lower()
    if "wins" in q3 or "take the pot" in q3 or "last player" in q3:
        print(f"{GREEN}Correct! If all other players fold, the last remaining player wins the pot without needing to show their cards.{RESET}")
    else:
        print(f"{RED}Incorrect! The correct answer is that the last player standing wins the pot immediately.{RESET}")
    t.sleep(2)
    input(f"{LIGHT_BLUE}Press Enter to continue...{RESET}")

def postLessonActivity(user_name):
    questions = [
    "At the showdown, two players reveal their hands: Player A has 2-4-8-7-10 all clubs, and Player B has 3-3-9-9-9 of different suits. Who wins and why? ",
    "How do the forced bets (small blind and big blind) influence player strategy and decision-making before the flop?",
    "Two players both have a Full House at showdown. What steps would you take to determine who wins the pot? Can you think of a situation where both players would split the pot?",
    "Give an example of a hand that consists of a straight flush.",
    "You have a 7 of clubs and a 9 of hearts. After the river, the board reads 6-4-8-7-10. What hand do you have?",
    "What is the difference between a flush and a straight flush?",
    "You have the following hole cards: 10 and J of Spades\nThe community cards after the turn are:♠️ Q of spades, K of Spades, 3 of Diamonds, 5 of Spades\nWhat card do you hope to see on the river to complete the strongest possible hand? Explain why."
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

# lesson 1: 扑克牌的基本知识
def start(user_data):
    user_name = user_data.get("name")
    print(f"{YELLOW}"+"="*50)
    t.sleep(1)
    print(f"{GREEN}Hey {user_name}! In this lesson, we will learn the basic knowledge of poker.")
    t.sleep(2)
    # Lesson 1 objectives:
    print(f"{CYAN}By the end of this lesson you should know the following:")
    t.sleep(1.5)
    print(f"\t{PURPLE}Memorize Hand Rankings{RESET}")
    t.sleep(1.5)
    print(f"\t{RED}Learn the Basic Game Structure of Texas Hold em")
    t.sleep(1.5)
    print(f"\t{BLUE}Understand the Basic Rules of Poker")
    t.sleep(1.5)
    user_input = input(f"Do you want a refresher on the contents of a standard deck of cards? ({GREEN}y{RESET}/{RED}n{RESET})").lower()
    if user_input == "y":
        card_refresher(user_name)
    else:
        t.sleep(1)
        print(f"Let's continue to the {CYAN}objectives of poker{RESET}!")
        t.sleep(1)
    
    # Objectives of poker:
    objectives_of_poker(user_name)
    # Hand rankings:
    hand_rankings(user_name)
    poker_hand_questions(user_name)
    print(f"{LIGHT_BLUE}Now that you understand poker hands, let's go over how a hand of Texas Hold'em is played!{RESET}")
    t.sleep(2)
    structure_of_texas_hold_em(user_name)
    game_flow_questions(user_name)
    postLessonActivity(user_name)
    input(f"{LIGHT_GREEN}Great job! {LIGHT_BLUE} Press Enter to return to the main menu{RESET}")
    user_data["lesson1"] = True
    return user_data


if __name__ == "__main__":
    start("Dude")