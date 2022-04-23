from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="secret_sauce",
)

csrf = CSRFProtect()
csrf.init_app(app)

from demo import routes




