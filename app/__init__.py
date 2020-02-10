from flask import Flask
from config import Config

app = Flask(__name__)

#Set the secret key to some random bytes.Keep this really secret!
app.config.from_object(Config)
 
from app import routes