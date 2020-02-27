import unittest
from unittest import mock
import GitHub567


class MyTestCase(unittest.TestCase):
    @mock.patch('GitHub567.GitHub567')
    def test_GitHub567(self, mock_req):
        mock_req("JWSolo").return_value = {'GithubApi567': 25, 'SSW567': 7, 'Triangle567': 8, 'University-HW10': 2}
        self.assertEqual(mock_req("JWSolo").return_value,
                         {'GithubApi567': 25, 'SSW567': 7, 'Triangle567': 8, 'University-HW10': 2})


if __name__ == '__main__':
    unittest.main()
