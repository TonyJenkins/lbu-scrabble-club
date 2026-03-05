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


if __name__ == "__main__":
    from member import Member

    alice = Member(1, 'Alice', 'Al', [150, 275, 160, 298])
    brian = Member(2, 'Brian', 'Bri', [100, 285, 240, 300])
    celia = Member(3, 'Celia', 'Celia', [302, 285, 290, 308])

    lb = LeaderBoard()
    lb.add_player(alice)
    lb.add_player(brian)
    lb.add_player(celia)

    lb.sort_board()
    lb.display_board()
