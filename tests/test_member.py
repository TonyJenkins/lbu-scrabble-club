import unittest

from scrabble_club.member import Member

class MemberTests(unittest.TestCase):
    def test_init_sets_fields_and_empty_games(self):
        member = Member(10, "Jane Doe", "JD")

        self.assertEqual(member.member_id, 10)
        self.assertEqual(member.name, "Jane Doe")
        self.assertEqual(member.nick_name, "JD")
        self.assertEqual(member.games, [])

    def test_init_with_games_parameter(self):
        games = [250, 300, 275]
        member = Member(11, "John Doe", "JD", games)

        self.assertEqual(member.member_id, 11)
        self.assertEqual(member.name, "John Doe")
        self.assertEqual(member.nick_name, "JD")
        self.assertEqual(member.games, games)
        self.assertEqual(member.average_score, 275.0)
        self.assertEqual(member.best_score, 300)

    def test_average_score_is_zero_when_no_games(self):
        member = Member(1, "A", "A")
        self.assertEqual(member.average_score, 0)

    def test_play_game_appends_score_and_updates_average(self):
        member = Member(2, "B", "Bee")

        member.play_game(200)
        member.play_game(300)
        member.play_game(250)

        self.assertEqual(member.games, [200, 300, 250])
        self.assertEqual(member.average_score, 250)

    def test_play_game_updates_best_score(self):
        member = Member(2, "B", "Bee")

        member.play_game(200)
        member.play_game(300)
        member.play_game(250)

        self.assertEqual(member.best_score, 300)
        member.play_game(350)

        self.assertEqual(member.best_score, 350)

        member.play_game(150)
        self.assertEqual(member.best_score, 350)

    def test_equality_uses_average_score(self):
        first = Member(3, "First", "F")
        second = Member(4, "Second", "S")

        for score in [200, 300]:
            first.play_game(score)
        for score in [100, 400]:
            second.play_game(score)

        self.assertTrue(first == second)

    def test_less_than_uses_average_score(self):
        lower = Member(5, "Lower", "L")
        higher = Member(6, "Higher", "H")

        for score in [150, 250]:
            lower.play_game(score)
        for score in [350, 450]:
            higher.play_game(score)

        self.assertTrue(lower < higher)

    def test_str_and_repr_formats(self):
        member = Member(7, "Sam", "S")
        member.play_game(300)
        member.play_game(360)

        self.assertEqual(str(member), "7, Sam, S, 330.0")
        self.assertEqual(
            repr(member),
            "Member(member_id=7, name='Sam', nick_name='S', games=[300, 360])",
        )


if __name__ == "__main__":
    unittest.main()
