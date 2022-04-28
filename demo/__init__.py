from flask import Flask
from flask_wtf import CSRFProtect
import secrets
app = Flask(__name__)
app.config.update(
    DEBUG=False,
    SECRET_KEY='2233asdfQAQ',
)

csrf = CSRFProtect()
csrf.init_app(app)





