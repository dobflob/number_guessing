import random
import statistics

"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
# define a custom error to display when a player's guess is outside the defined range
class OutsideRangeError(Exception):
    def __init__(self, message):
        self.message = message

# show_instructions shows the player game instructions that can be requested during game play
def show_instructions():
    print("""
          Welcome to the Number Guessing Game - The rules are simple:

          * Enter a whole number 1-100
          * 'Lower' means the winning number is lower than your guess
          * 'Higher' means the winning number is higher than your guess
          * Guess until you get it right or until you're ready to give up.
          * Type 'Help' to view the instructions
          * Type 'New' to start over
          * Type 'Quit' to quit
          """)
    
def print_high_score():
    print(f'\nCurrent High Score: {min(player_scores)}\n')

# Player scores stores all scores from a player's active session
player_scores = []

# Max number and Min number are used to define the range
max_number = 100
min_number = 1

def set_winning_number():
    return random.randint(min_number, max_number + 1)

def start_game():
    # Show instructions
    show_instructions()

    # number of guesses increments as the user enters valid guesses; invalid values don't count against your score
    num_of_guesses = 0
    player_guess = ''
    
    # winning number is generated as a pseudo random integer between the min and max numbers
    winning_number = set_winning_number()    

    while True:
        player_guess = input('>>  ').lower()

        if player_guess == 'help':
            show_instructions()
        elif player_guess == 'quit':
            print('\nThanks for playing.\n')
            break
        elif player_guess == 'new':
            num_of_guesses = 0
            winning_number = set_winning_number()
            if player_scores:
                print_high_score()
        else:
            try:
                # If the player's guess is an integer, check to ensure it's within the range
                # If the guess is within the correct range, compare the number to the winning number and provide feedback about the player's guess. Finally, increment the guess count by 1 for each valid guess.
                player_guess = int(player_guess)
                
                if player_guess < min_number or player_guess > max_number:
                    raise OutsideRangeError(f'Your guess is outside the range of {min_number}-{max_number}. Please try again.')
                elif player_guess > winning_number:
                    print('Lower')
                    num_of_guesses += 1
                elif player_guess < winning_number:
                    print('Higher')
                    num_of_guesses += 1
                elif player_guess == winning_number:
                    # When the game ends, add the score to the player scores array to be used for statistical analysis
                    num_of_guesses += 1
                    player_scores.append(num_of_guesses)

                    print(f"""
                        Congrats! You guessed the winning number in {num_of_guesses} attempts.

                        Player Data:
                            * Games Played: {len(player_scores)}
                            * Mean Attempts: {sum(player_scores) / len(player_scores)}
                            * Median Attempts: {statistics.median(player_scores)}
                            * Mode Attempts: {statistics.mode(player_scores)}
                        """)
                    play_again = input('Do you want to play again? Y/N  ')

                    # If the player opts to play again, the game starts over. Otherwise, the game ends.
                    if play_again.lower() == 'y':
                        num_of_guesses = 0
                        winning_number = set_winning_number()
                        print_high_score()
                    else:
                        print('\nThanks for playing!\n')
                        break
            except ValueError:
                print('Invalid Value. Please try again or enter "Help" for help.')
            except OutsideRangeError as err:
                print(err.message)
            except Exception:
                print('Uh oh! Something unexpected happened.')

start_game()