import unittest
from unittest.mock import patch
from main import main, web_renderer

class TestMainFunction(unittest.TestCase):
    @patch('main.web_renderer')
    def test_main_function(self, mock_web_renderer):
        main()
        mock_web_renderer.assert_called_once()
        mock_web_renderer.return_value.run.assert_called_once()

if __name__ == '__main__':
    unittest.main()