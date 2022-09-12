import random


def rules():
    """
    Rules of the game.
    """
    print("        WELCOME TO ALIEN INVASION...!\n")
    print("Hello Earhling, we are from the plant Alshabaa...\n")
    print("We have been watching Earth for many years...\n")
    print("It seems humans have ruined your planet...\n")
    print("So we are here to take over...!\n")
    print("If you want to stop us from invading...\n")
    print("You need to guess which country we intend to invade first.\n")
    print("But beware... You can only guess wrong 6 times...\n")
    welcome()


def intro():
    """
    Opening text welcoming the user
    Gives options for rules or to play the game
    """
    print("         ALIEN INVASION 2022...!!\n")
    print("Hello Earthling. What would you like to do?")
    print("Enter 1 for rules or anything else to play the game.\n")
    user_input = input("Please enter your option: ")
    if user_input == "1":
        rules()
    else:
        welcome()

#def welcome():



#def play_again():


#def create_random_country():


def game_start():
    intro()


game_start()
