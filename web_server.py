import util
from datetime import datetime
import os
import json
from abc import ABC, abstractmethod
from flask import Flask

class web_server(ABC):
    app = Flask(__name__, template_folder=f"{util.get_data_folder()}/templates/")
    def __init__(self):
        pass
                
    def run(self):
        web_server.app.run(port=8080, debug=True)
        
    @abstractmethod    
    def render_page(content_name, text=None):
        pass

    @abstractmethod
    def home():
        pass



