from hangman.game import Game
from hangman.game_status import GameStatus


def chars_list_to_string(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

print(f"The word consist {len(game.word)}")
print("Try to guess the word letter by letter")

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input("Pick a letter.\n")
    state = game.guess_letter(letter)

    print(chars_list_to_string(state))

    print(f"Remaining tries = {game.remaining_tries}")
    print(f"Tried letter: {chars_list_to_string(game.tried_letters)}")

if game.game_status == GameStatus.LOST:
    print("You are hanged")
    print(f"The word was: {game.word}")
else:
    print("You won!")
