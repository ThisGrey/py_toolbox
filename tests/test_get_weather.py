from io import StringIO
import unittest
from unittest.mock import patch
from scripts.get_weather import load_settings, is_valid_plz, get_weather

class TestGetWeather(unittest.TestCase):
    @patch('builtins.input', side_effect=['12345'])
    def test_get_weather_success(self, mock_input):
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {
                'name': 'Berlin',
                'main': {'temp': 20.0},
                'weather': [{'description': 'Clear sky'}]
            }

            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                load_settings()
                self.assertTrue(is_valid_plz('12345'))
                self.assertTrue(get_weather('fake_api_key', '12345'))

            expected_output = (
                "Weather in Berlin:\n"
                "Temperature: 20.0°C\n"
                "Description: Clear sky\n"
                "---------------------------\n"
            )
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['invalid'])
    def test_get_weather_invalid_plz(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            load_settings()
            self.assertFalse(is_valid_plz('invalid'))
            self.assertFalse(get_weather('fake_api_key', 'invalid'))

        expected_output = "Error: Invalid PLZ. Please enter a valid German postal code.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['12345'])  
    def test_get_weather_error(self, mock_input):
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 404

            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                load_settings()
                self.assertTrue(is_valid_plz('12345'))
                self.assertFalse(get_weather('fake_api_key', '12345'))

            expected_output = "Error: Unable to retrieve weather data. Status code: 404\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()