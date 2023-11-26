import random
# https://www.youtube.com/watch?v=XWuP5Yf5ILI
print("Welcome to Hangman!")

words = ["hacker", "bounty", "random"]
secret_word = random.choice(words)
guess_time = 5
#print("You get "+ str(guess_time) + " guesses")
print(f"You get {guess_time} guesses")  # update to lastrer than python 3.6
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

# create a variable as an int starting as 0 and when it gets to
#  the number 5 the game ends
# add a print statement tell the user they get 5 guesses

num = 0
game_over = False

while not game_over:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f"You have {guesses_left} guesses left")
        if num >= 5:
            print("You Loser")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win")
        game_over = True