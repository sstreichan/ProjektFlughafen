import unittest
from web_renderer import web_renderer
from unittest.mock import Mock


class TestWebRenderer(unittest.TestCase):
    def test_filter_data(self):
        test_data = {
            "1": {"flugdaten": {"key1": "value1", "key2": "value2"}},
            "2": {"flugdaten": {"key1": "value3", "key2": "value4"}}
        }
        web_renderer_instance = web_renderer()
        result = web_renderer_instance.filter_data(test_data, "value1")
        self.assertEqual(result, {"1": {"flugdaten": {"key1": "value1", "key2": "value2"}}})

    
if __name__ == '__main__':
    unittest.main()
    
    