"""
main module
"""
from web_renderer import web_renderer

import datenbank_funktionen


def main():
    app = web_renderer()    
    app.run()


if __name__ == "__main__":
    main()
