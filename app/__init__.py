from flask import Flask
from config import Config

app = Flask(__name__)

#Set the secret key to some random bytes.Keep this really secret!
app.config.from_object(Config)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(debug=True, host='0.0.0.0')
 
from app import routes