#!/usr/bin/env python3

class LeaderBoard:

    def __init__(self, **kwargs):
        if 'competition' in kwargs:
            self.competition = kwargs['competition']
        else:
            self.competition = None

        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def sort_board(self):
        self.players.sort(reverse=True)

    def display_board(self):
        if self.competition:
            print(f'{self.competition.title()} Competition')
            print()
        print(self)

    def __str__(self):
        from tabulate import tabulate

        headers = ["Name", "Average Score", "Best Score"]
        return tabulate([player.board_entry for player in self.players], headers=headers, tablefmt="fancy_grid")

