from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fishing is great!'
from demo import routes




