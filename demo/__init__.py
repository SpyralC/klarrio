from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

from demo import routes




