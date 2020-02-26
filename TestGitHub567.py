from GitHub567 import GitHub567
import unittest


class TestCase(unittest.TestCase):

    def test_Github567(self):
        self.assertEqual(GitHub567("JWSolo"), {'GithubApi567': 21, 'SSW567': 7, 'Triangle567': 8, 'University-HW10': 2})


if __name__ == "__main__":
    print("Test goes down here:")
    unittest.main()
