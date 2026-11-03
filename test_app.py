import unittest

from app import app


class HomeRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_route_returns_welcome_message(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Welcome to the Coursera CI/CD Final Project!", response.data
        )


if __name__ == "__main__":
    unittest.main()
