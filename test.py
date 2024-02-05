import unittest
from flask import json
from app import app

class WeatherAPITestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_weather_success(self):
        response = self.app.post('/weather', json={"city": "New York"})
        data = self.get_json(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn('main', data, "Weather data not present in response.")

    def test_get_weather_error(self):
        response = self.app.post('/weather', json={})
        data = self.get_json(response)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data, "Error message not present in response.")

    def get_json(self, response):
        return response.get_data(as_text=True)

if __name__ == '__main__':
    unittest.main()
