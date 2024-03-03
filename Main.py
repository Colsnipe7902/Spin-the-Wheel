import random

def spin_wheel():
    return random.randint(1, 12)

def play_game():
    user_score = 0
    ai_score = 0

    while user_score < 50 and ai_score < 50:
        input("Press Enter to spin the wheel...")
        
        user_guess = int(input("Enter your guess (1-12): "))
        ai_guess = random.randint(1, 12)

        user_spin = spin_wheel()
        ai_spin = spin_wheel()

        print(f"You spun {user_spin}, AI spun {ai_spin}")

        if user_spin == user_guess:
            user_score += 1
            print(f"Correct guess! You earned 1 point. Your score: {user_score}")
        else:
            print("Incorrect guess!")

        if ai_spin == ai_guess:
            ai_score += 5
            print(f"AI made a correct guess! AI earned 1 point1. AI's score: {ai_score}")
        else:
            print("AI made an incorrect guess!")

    if user_score >= 50:
        print("Congratulations! You won!")
    else:
        print("AI won. Better luck next time.")
