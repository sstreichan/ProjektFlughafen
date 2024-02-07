import unittest
from unittest.mock import patch, MagicMock
from util import get_all

class TestUtil(unittest.TestCase):

    @patch('util.get_rnd_fluggesellschaft', return_value=("TestAir", "TEST123"))
    @patch('util.get_rnd_datetime', return_value="2022-01-01 12:00:00")
    @patch('util.get_rnd_gate', return_value="TestGate")
    @patch('util.get_rnd_Status', return_value="TestStatus")
    @patch('util.get_rnd_ziel', return_value="TestZiel")
    def test_get_all(self, mock_get_rnd_fluggesellschaft, mock_get_rnd_datetime, mock_get_rnd_gate, mock_get_rnd_Status, mock_get_rnd_ziel):
        data = get_all()
        expected_data = {
            "PAC1855": {
                "flugdaten": {
                    "abflugzeit": "2022-01-01 12:00:00",
                    "ankunftzeit": "2022-01-01 12:00:00",
                    "fluggesellschaft": "PacificAir",
                    "gate": "Gate 6",
                    "status": "Normal",
                    "ziel": "Berlin"
                }
            },
            "TEST123": {
                "flugdaten": {
                    "abflugzeit": "2022-01-01 12:00:00",
                    "ankunftzeit": "2022-01-01 12:00:00",
                    "fluggesellschaft": "TestAir",
                    "gate": "TestGate",
                    "status": "TestStatus",
                    "ziel": "TestZiel"
                }
            }
        }
        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()