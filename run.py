import random
import countries
import alien
import string

print(alien.LOGO)


def rules():
    """
    Rules of the game.
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
    Opening text welcoming the user
    Gives options for rules or to play the game
    """
    print("         ALIEN INVASION 2022...!!\n")
    print("Hello Earthling. What would you like to do?")
    print("Enter 1 for rules or anything else to play the game.\n")
    user_input = input("What option would you like: ")
    print("\n")
    if user_input == "1":
        rules()
    else:
        welcome()

def welcome():
    """
    Asks user for name.
    Asks user for letters for name only
    """
    print(alien.LOGO)
    print("Before we start, please tell us your name.\n")
    user = input("What is your name Earthling?\n").capitalize()

    if user.isalpha() == True:
        print(f"Greetings {user}...\n")
        print("What country do you think we will invade first...?\n")

    else:
        print(
            "Not a valid input. Only use letters, "
            "Please try again"
            )
        user = input("What is your name Earthling?\n").capitalize()
        

#def play_again():


def create_random_country():
    """
    Generates the country that the user will be guessing
    Pulls the country_list from the countries file
    And chooses a country at random
    """
    random_country = countries.country_list
    return random.choice(random_country).upper()


def main():
    """
    Initiates game and incorporates game loop
    """
    intro()

    # Variables needed for game play
    country = create_random_country()

    guessed_letters = []

    remaining_attempts = 6

    guessed = False

    alphabet = string.ascii_uppercase

    # Print a number of _ equal to the letters in the country to guess
    print("The country contains", len(country), "letters")
    print(len(country) * (" _ "))

    while guessed == False and remaining_attempts > 0:
        print("You have " + str(remaining_attempts) + " guesses left.\n")
        guess = input("Guess a letter: ").upper()

        if len(guess) == 1:
            if guess not in alphabet:
                print("Check your entry. Use letters only")
            elif guess in guessed_letters:
                print("You have already guessed that. Try again..!")
            elif guess not in country:
                print("Bad luck Earthling That letter is wrong")
                guessed_letters.append(guess)
                remaining_attempts -= 1
            elif guess in country:
                print("Well done... That letter is correct")
                guessed_letters.append(guess)
            else:
                print("Check you entry... Invalid input")

        else:
            if len(guess) != 1:
                print("Whoa there Earthling.. Only 1 letter at a time")

        status = ""
        if guessed == False:
            for letter in country:
                if letter in guessed_letters:
                    status += letter
                else:
                    status += "_"
            print(status)

        if status == country:
            print(
                "Congratulations... You guessed the right country "
            "and stopped the Alien Invasion...!!!"
            )
            guessed = True
        elif remaining_attempts == 0:
            print("Oh No... You couldn't stop the Alien Invasion")

        print(alien.ALIENS[remaining_attempts])

main()
