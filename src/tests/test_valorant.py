import unittest

import valorant

# python setup.py test


class TestValorant(unittest.TestCase):

    # should return a json object if player is found
    def test_get_player_json(self):
        self.assertNotEqual(valorant.get_player_json("MayNiklas", "Niki"), None)

    # should return None if player not found
    def test_get_player_json_fail(self):
        self.assertEqual(valorant.get_player_json("not", "existent"), None)

    # test if get_elo returns a number
    def test_get_elo(self):
        self.assertGreaterEqual(
            valorant.get_elo(valorant.get_player_json("MayNiklas", "Niki")), 0
        )

    # test if get_elo returns a None if player not found
    def test_get_elo_fail(self):
        self.assertEqual(valorant.get_player_json("not", "existent"), None)

    # test if get_rank returns a string
    def test_get_rank(self):
        self.assertIsInstance(
            valorant.get_rank(valorant.get_player_json("MayNiklas", "Niki")), str
        )

    # todo: test if get_rank returns a None if player not found (code not implemented yet)
    # def test_get_rank_fail(self):
    #     self.assertEqual(
    #         valorant.get_rank(valorant.get_player_json("not", "existent")), None
    #     )


if __name__ == "__main__":
    unittest.main()
