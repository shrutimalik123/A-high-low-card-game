import random

def high_low_game():
    ## 1. Setup the Deck
    # Cards are represented by their value. (Aces=1, J=11, Q=12, K=13)
    deck_values = list(range(1, 14)) * 4  # Four suits of values 1-13
    random.shuffle(deck_values) # Shuffle the deck
    
    # Simple mapping for better display
    card_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    
    score = 0
    print("--- ♥️ High-Low Card Game ♦️ ---")
    print("Guess if the next card will be Higher or Lower than the current one.")

    # Start with the first card
    current_card_value = deck_values.pop() # Get the last card and remove it from the deck
    
    # Use the name map for display, or just the number
    current_card_display = card_names.get(current_card_value, str(current_card_value))
    print(f"\nYour starting card is: **{current_card_display}**")

    ## 2. Main Game Loop
    # Keep playing as long as there are cards left and the player hasn't quit
    while len(deck_values) > 0:
        print("\n-------------------------------------")
        print(f"Current Score: {score}")

        # Get the next card without removing it yet
        next_card_value = deck_values[-1] 
        
        # Get player input
        guess = input("Will the next card be [H]igher or [L]ower? (or 'Q' to quit): ").strip().lower()

        if guess == 'q':
            break

        if guess not in ('h', 'l'):
            print("Invalid input. Please enter 'H', 'L', or 'Q'.")
            continue

        # Now remove the card from the deck and get its display name
        next_card_value = deck_values.pop()
        next_card_display = card_names.get(next_card_value, str(next_card_value))
        
        print(f"The next card is: **{next_card_display}**")

        ## 3. Comparison Logic
        
        is_higher = next_card_value > current_card_value
        is_lower = next_card_value < current_card_value

        if is_higher and guess == 'h':
            print("✅ Correct! The next card was HIGHER.")
            score += 1
        elif is_lower and guess == 'l':
            print("✅ Correct! The next card was LOWER.")
            score += 1
        elif next_card_value == current_card_value:
            print("⚠️ It was a tie! No change in score.")
        else:
            print("❌ Incorrect guess.")
            print(f"The correct answer was {'HIGHER' if is_higher else 'LOWER'}.")
            break # Game over on a wrong guess

        # Update the current card for the next round
        current_card_value = next_card_value
        current_card_display = next_card_display
        
        # If the loop continues, the new current card is set.

    ## 4. Game Conclusion
    print("\n=====================================")
    print(f"Game over! Your final score is **{score}**.")
    if len(deck_values) == 0:
        print("You guessed your way through the entire deck! Incredible!")

# Start the game
high_low_game()
