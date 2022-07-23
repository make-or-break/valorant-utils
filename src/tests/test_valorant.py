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


if __name__ == "__main__":
    unittest.main()
