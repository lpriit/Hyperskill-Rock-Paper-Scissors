import random


class RockPaperScissors:
    list_options = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.computer = ''
        self.player = ''
        self.player_name = ''
        self.scores = {}
        self.score = 0
        self.list_options = ['rock', 'paper', 'scissors']

    def main_menu(self):
        pass

    def input_options(self, options):
        if options != '':
            self.list_options = list(options.split(','))

    def custom_winner(self):
        if self.player == self.computer:
            print('There is a draw ({})'.format(self.player))
            self.score += 50
        else:
            winners = self.winning_options()
            # print(winners)
            if self.computer not in winners:
                print('Well done. The computer chose {} and failed'.format(self.computer))
                self.score += 100
            else:
                print('Sorry, but the computer chose {}'.format(self.computer))

    def winning_options(self):
        if self.list_options.index(self.player) + int((len(self.list_options) - 1) / 2) <= len(self.list_options):
            winning_options = self.list_options[
                              self.list_options.index(self.player) + 1:self.list_options.index(self.player) + int(
                                  (len(self.list_options) - 1) / 2) + 1]
            return winning_options
        else:
            options_to_remove = self.list_options[
                              self.list_options.index(self.player) -
                              int((len(self.list_options) - 1) / 2):self.list_options.index(self.player)]
            winning_options = list(self.list_options)
            for item in options_to_remove:
                winning_options.remove(item)
            winning_options.remove(self.player)
            return winning_options

    def print_scores(self):
        # print(self.scores)
        # print('--')
        print('Your rating: {}'.format(self.score))
        self.human_input()

    def results_parser(self):
        file = open('rating.txt', 'r')
        for line in file:
            split_line = line.rstrip('\n').split(' ')
            self.scores[split_line[0]] = int(split_line[1])
        if self.player_name in self.scores:
            self.score = self.scores[self.player_name]
        file.close()

    def human_input(self):
        human_input = input()
        if human_input in self.list_options:
            self.player = human_input
            self.computer_play()
            # self.winner()
            self.custom_winner()
            self.winning_options()
            self.human_input()
        elif human_input == '!exit':
            print('Bye!')
        elif human_input == '!rating':
            self.print_scores()
        else:
            print('Invalid input')
            self.human_input()

    def computer_play(self):
        self.computer = random.choice(self.list_options)

    def winner(self):
        if self.computer == self.player:
            print('There is a draw ({})'.format(self.computer))
            self.score += 50
        elif ((self.player == 'paper' and self.computer == 'rock') or
              (self.player == 'scissors' and self.computer == 'paper') or
              (self.player == 'rock' and self.computer == 'scissors')):
            print('Well done. The computer chose {} and failed'.format(self.computer))
            self.score += 100
        else:
            print('Sorry, but the computer chose {}'.format(self.computer))


rock_paper_scissors = RockPaperScissors()
rock_paper_scissors.player_name = input('Enter your name: ')
print('Hello, {}'.format(rock_paper_scissors.player_name))
rock_paper_scissors.input_options(input())
print('Okay, let\'s start')
# rock_paper_scissors.player_name(player_name)
rock_paper_scissors.results_parser()
# rock_paper_scissors.print_scores()
rock_paper_scissors.human_input()


