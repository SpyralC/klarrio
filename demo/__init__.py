from flask import Flask
from flask_wtf import CSRFProtect
app = Flask(__name__)
app.config.update(
    DEBUG=False,
    SECRET_KEY="jimmy23333QAQ"
)

csrf = CSRFProtect()
csrf.init_app(app)





