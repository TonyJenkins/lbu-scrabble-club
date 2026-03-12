#!/usr/bin/env python3


class Member:

    def __init__(self, member_id, name, nick_name, games=None):
        self.member_id = member_id
        self.name = name
        self.nick_name = nick_name

        self.games = games if games else []

    def play_game(self, new_score):
        self.games.append(new_score)

    @property
    def average_score(self):
        if self.games:
            return sum(self.games) / len(self.games)
        else:
            return 0

    @property
    def best_score(self):
        if self.games:
            return max(self.games)
        else:
            return 0

    @property
    def board_entry(self):
        return [f'{self.name} ({self.nick_name})', self.average_score, self.best_score]

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __str__(self):
        return f"{self.member_id}, {self.name}, {self.nick_name}, {self.average_score}"

    def __repr__(self):
        return (
            f"Member(member_id={self.member_id!r}, name={self.name!r}, "
            f"nick_name={self.nick_name!r}, games={self.games!r})"
        )
