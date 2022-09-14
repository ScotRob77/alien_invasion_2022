import random
import countries
import alien
import string

"""
Credit to https://mardiyyah.medium.com/ for game idea and parts of code
"""


def clear():
    print("\033c")


def rules():
    """
    Rules of the game.
    Following the rules is the welcome function requesting the user
    to enter their name.
    """
    print("        WELCOME TO ALIEN INVASION...!\n")
    print("Hello Earthling, we are from the plant Alshabaa...\n")
    print("We have been watching Earth for many years...\n")
    print("The human race has ruined the planet...\n")
    print("So we are here to take over...!\n")
    print("If you want to stop us from invading...\n")
    print("You need to guess which country we intend to invade first.\n")
    print("But beware... You can only guess wrong 6 times...\n")
    welcome()


def intro():
    """
    Opening text where the user is given two options
    The option to read the rules or to play the game
        The if statement validates user input
        else takes user to welcome function
    Returns:
        The rules or welcome message
    """
    print("         ALIEN INVASION 2022...!!\n")
    print("Hello Earthling. What would you like to do?")
    print("Enter 1 for rules or anything else to play the game.\n")
    user_input = input("What option would you like: ")
    print("\n")
    if user_input == "1":
        clear()
        rules()
    else:
        clear()
        welcome()


def welcome():
    """
    Asks user for name.
    Asks user for letters for name only
        if statement validates user input
        else asks user to input name again
    Returns:
        user enters name in correct format they are asked what country they
        think will be invaded first
        if not welcome function initiated again
    """
    print(alien.LOGO)
    print("Before we start, please tell us your name.\n")
    user = input("What is your name Earthling?\n").strip().capitalize()
    print()

    if user.isalpha():
        print(f"Greetings {user}...\n")
        print("What country do you think we will invade first...?\n")

    else:
        print("Please enter your name using letters only")
        welcome()


def play_again_winner():
    """
    Function for asking the user if they want to play again
    """
    response = input(
        "Do you think you could stop them again...?\n"
        "\nEnter 'y' to play again: ")
    if response == "y":
        clear()
        main()
    else:
        print()
        print("Hope you enjoyed playing.. See you again soon")


def play_again_loser():
    """
    Function for asking the user if they want to play again
    """
    response = input(
        "But there may still be time to stop them...\n\n"
        "Would you like to try again...? Enter 'y' to play again: "
    )
    if response == "y":
        clear()
        main()
    else:
        print()
        print("Hope you enjoyed playing.. See you again soon")


def choose_random_country():
    """
    Pulls the country_list from the countries file
    And chooses a country at random
    Assigns to a variable

    Returns:
    A random country and converts to uppercase. The country
    returned is used in the game
    """
    random_country = countries.country_list
    return random.choice(random_country).upper()


def main():
    """
    Initiates game and starts game loop
    """
    print(alien.LOGO_TWO)

    intro()

    """
    Variables needed for game play
    """
    country = choose_random_country()

    guessed_letters = []

    remaining_attempts = 6

    guessed = False

    alphabet = string.ascii_uppercase

    """
    Prints a number of _ equal to the letters in the country to guess
    """
    print("The country contains", len(country), "letters")
    print(len(country) * (" _ "))

    while not guessed and remaining_attempts > 0:
        print("You have " + str(remaining_attempts) + " guesses left.\n")

        guess = input("Guess a letter: ").strip().upper()
        print()

        if len(guess) != 1:
            print("Whoa there Earthling.. Only 1 letter at a time")
            continue

        if guess not in alphabet:
            print("Check your entry. Use letters only")
            continue

        if guess in guessed_letters:
            print("You have already guessed that. Try again..!")
            continue

        if guess in country:
            print(f"Well done... {guess} is correct")
            guessed_letters.append(guess)

        else:
            print(f"Bad luck...! {guess} is wrong")
            guessed_letters.append(guess)
            remaining_attempts -= 1

        print(alien.ALIENS[remaining_attempts])

        status = ""
        if not guessed:
            for letter in country:
                if letter in guessed_letters:
                    status += letter
                else:
                    status += " _ "
            print(status)

        if status == country:
            print(
                "CONGRATULATIONS... You guessed the right country "
                "and stopped the Alien Invasion...!!!\n"
            )
            guessed = True
            play_again_winner()
        elif remaining_attempts == 0:
            print("You Lose..! Aliens have invaded and are taking over.\n")
            play_again_loser()


if __name__ == "__main__":
    main()
