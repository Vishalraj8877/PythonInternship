import random

def hangman():
    words = ['python', 'program', 'computer', 'hangman', 'keyboard', 'internet', 'function', 'variable']
    word = random.choice(words)
    word_letters = set(word)
    guessed_letters = set()
    tries = 6  # Number of allowed incorrect guesses

    print("🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"You have {tries} incorrect guesses allowed.\n")

    while tries > 0 and word_letters:
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word: ", ' '.join(display_word))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("❗ You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Correct guess!\n")
        else:
            tries -= 1
            print(f"❌ Incorrect guess! Tries left: {tries}\n")

    if not word_letters:
        print(f"🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"💀 Game Over! The correct word was: {word}")

# Run the game
hangman()
