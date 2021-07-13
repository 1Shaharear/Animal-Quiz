## Animal Quiz by Shaharear
def check_guess(guess, answer):
    global score
    still_guessing = True
    a = 0
    while still_guessing and a < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if a < 2:
                guess = input("Sorry Wrong Answer, try again")
            a = a + 1
    if a == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the national animal of Bangladesh?")
check_guess(guess2, "Tiger")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
guess4 = input("Which is the tallest animal on Earth? ")
check_guess(guess4, "Giraffes")
print("Your Score is "+ str(score))
