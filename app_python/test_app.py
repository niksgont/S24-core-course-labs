import unittest
from app import home


class TestApp(unittest.TestCase):
    def test_moscow_time(self):
        result = home()
        self.assertIn("Current Time in Moscow:", result)


if __name__ == "__main__":
    unittest.main()
