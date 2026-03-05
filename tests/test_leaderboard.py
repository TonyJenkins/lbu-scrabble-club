#!/usr/bin/env python3

import unittest

from scrabble_club.leaderboard import LeaderBoard
from scrabble_club.member import Member


class LeaderBoardTests(unittest.TestCase):
    def setUp(self):
        self.board = LeaderBoard()

    def test_init_without_competition(self):
        board = LeaderBoard()
        self.assertEqual(board.competition, None)
        self.assertEqual(board.players, [])

    def test_init_with_competition(self):
        board = LeaderBoard(competition="Spring 2026")
        self.assertEqual(board.competition, "Spring 2026")
        self.assertEqual(board.players, [])

    def test_add_player_single(self):
        member = Member(1, "Alice", "Ace")
        self.board.add_player(member)

        self.assertEqual(len(self.board.players), 1)
        self.assertEqual(self.board.players[0], member)

    def test_add_multiple_players(self):
        alice = Member(1, "Alice", "Ace")
        bob = Member(2, "Bob", "Bobby")
        carol = Member(3, "Carol", "Caz")

        self.board.add_player(alice)
        self.board.add_player(bob)
        self.board.add_player(carol)

        self.assertEqual(len(self.board.players), 3)
        self.assertEqual(self.board.players[0], alice)
        self.assertEqual(self.board.players[1], bob)
        self.assertEqual(self.board.players[2], carol)

    def test_sort_board_orders_by_score(self):
        low = Member(1, "Low Scorer", "L")
        low.play_game(200)
        low.play_game(250)

        mid = Member(2, "Mid Scorer", "M")
        mid.play_game(300)
        mid.play_game(350)

        high = Member(3, "High Scorer", "H")
        high.play_game(400)
        high.play_game(450)

        self.board.add_player(high)
        self.board.add_player(mid)
        self.board.add_player(low)

        self.board.sort_board()

        self.assertEqual(self.board.players[0], high)
        self.assertEqual(self.board.players[1], mid)
        self.assertEqual(self.board.players[2], low)

    def test_sort_board_with_equal_scores(self):
        alice = Member(1, "Alice", "A")
        alice.play_game(300)

        bob = Member(2, "Bob", "B")
        bob.play_game(300)

        self.board.add_player(bob)
        self.board.add_player(alice)

        self.board.sort_board()

        self.assertEqual(len(self.board.players), 2)
        self.assertIn(alice, self.board.players)
        self.assertIn(bob, self.board.players)


if __name__ == "__main__":
    unittest.main()

