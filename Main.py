from random import randint

def display_welcome_banner():
    welcome_banner = """
                Welcome to Spin the Wheel game!

        - It is a wheel-spinning game.
        
        - The wheel contains numbers from 1 to 12.

        - The game will be played in rounds between the computer and user.
        
        - Match the parity of the round number and spin number.
        
        - If the parity matches, the user gets one point.
       
        - Otherwise, the computer gets one point.

        - The game ends when one of the players reaches 50.
    """
    print(welcome_banner)

def get_spin_result():
    return randint(1, 12)

def is_even(number):
    return number % 2 == 0

def update_scores(user_score, computer_score, spin_result, round_number):
    spin_parity = "even" if is_even(spin_result) else "odd"
    
    print(f"Round number: {round_number}")
    print(f"You got: {spin_result}")
    print(f"User Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    if is_even(user_score) == is_even(spin_result):
        user_score += 1
        print(f"You scored! Spin result: {spin_result} ({spin_parity})")
    else:
        computer_score += 1
        print(f"Computer scored! Spin result: {spin_result} ({spin_parity})")

    print("-------------------------------------")

    return user_score, computer_score

def main():
    display_welcome_banner()

    user_name = input("Enter your name: ")

    user_score = 0
    computer_score = 0
    round_number = 1
    still_playing = True

    while still_playing:
        input("Spin the wheel (press enter): ")
        spin_result = get_spin_result()
        user_score, computer_score = update_scores(user_score, computer_score, spin_result, round_number)

        round_number += 1

        if user_score >= 50 or computer_score >= 50:
            still_playing = False

    if user_score >= 50:
        print(f"Congratulations {user_name}! You won!")
    else:
        print("Computer won. Better luck next time!")

if __name__ == "__main__":
    main()
