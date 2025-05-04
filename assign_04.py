#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 04, 25, 2025
# This program is displays the specific amount of phrases


def main():
    question_1 = input("Welcome, do you want to play a game?")
    # Greets and ask a first question
    if question_1.lower() != "yes":
        while True:
            print("Just enter yes.")
            question_2 = input("Welcome, do you want to play a game? ")
            if question_2.lower() == "yes" or question_2.lower() == "yes.":
                break
    phrase = input(
        "Enter your phrase, please."
    )  # Gets the phrase which will be repeated over and over
    user_amount = input(
        "How much times do you want your phrase to repeat?"
    )  # Gets amount for how much will the phrase repeat.
    counter = 0  # Sets the counter needed for loop operations
    try:  # Catches any wrong input
        user_amount = int(user_amount)
        for counter in range(
            user_amount + 1
        ):  # My second type of loop which takes key role in displaying the phrase
            print(phrase * counter)  # Prints off the phrase
            counter = counter + 1
    except Exception:
        print(
            "Need an integer for amount of phrases."
        )  # Prints this statement if the input for integer is not correct
    counter2 = 0  # Sets another counter for loop
    question_3 = input(
        "Do you want a joke?"
    )  # Asks the user if they want to here a joke
    while question_3.lower() != "yes":  # Makes a loop if user says no
        print("Come on, say yes. It will be funny.")
        question_3 = input(
            "Type yes."
        )  # Asks many times over so the user would say yes
        counter2 = counter2 + 1
        if counter2 >= 5:  # If the user said no 5 types or over it breaks the loop
            print("The joke is actually funny.")
            break
    print("What kind of music do bubbles hate? Pop.")


if __name__ == "__main__":
    main()
