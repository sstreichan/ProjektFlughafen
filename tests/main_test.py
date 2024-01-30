import unittest
from web_renderer import web_renderer
from flask import Flask

class TestWebRenderer(unittest.TestCase):

    def test_render_page():
        app = Flask(__name__, template_folder=f"../../templates/")
        # Create a web_renderer instance
        renderer = web_renderer()
        # Call the render_page method with some input and check for expected behavior
        self.assertIsNotNone(renderer.render_page("content_name", "text"))

    def test_home():
        # Create a web_renderer instance
        renderer = web_renderer()
        # Call the home_old method and check for expected behavior
        self.assertIsNotNone(renderer.home())

    # Add more test cases for other methods as needed

if __name__ == '__main__':
    unittest.main()