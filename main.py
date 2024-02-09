"""
main module
"""
from web_renderer import web_renderer

from Database import Database
import os

debug = True


def main():
    try:
        app = web_renderer()
        app.run()
    except KeyboardInterrupt:
        print("Programm wird beendet...")
        import sys
        sys.exit()
    except Exception as e:
        print(f"Der follgende Fehler ist aufgetreten: {e}")
        import sys
        sys.exit()


if __name__ == "__main__":
    main()
    
