import random

# List of predefined words
words = ["apple", "tiger", "chair", "robot", "house"]

# Choose a random word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Display hidden word
display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct!")

        # Replace blanks with correct letter
        for index in range(len(word)):
            if word[index] == guess:
                display_word[index] = guess

    # Wrong guess
    else:
        print("❌ Wrong!")
        wrong_guesses += 1

# Result
if "_" not in display_word:
    print("\n🎉 You Won!")
    print("The word was:", word)
else:
    print("\n💀 You Lost!")
    print("The word was:", word)