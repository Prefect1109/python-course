'''
    This is an example of final version of exercise
'''
import random




class GuessGame:

    def __init__(self, max_number: int, attempts_allowed: int):
        self.secret_number = random.randrange(1, max_number)
        self.attempts_allowed = attempts_allowed

    def run(self):
        for i in range(self.attempts_allowed):
            user_guess = self.get_user_guess()
            if user_guess == self.secret_number:
                print('YEEEEEEEEEAH')
                return
            print('NOOOOOO')
        print('GameOver')
    def get_user_guess(self) -> int:
        try:
            user_guess = int(input('Your guess \n'))
            return user_guess
        except ValueError:
            print('FK U')
            self.get_user_guess()


game = GuessGame(11, attempts_allowed=3)
game.run()
