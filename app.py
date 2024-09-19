from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['MONGO_DATABASE_URI'] = os.getenv('MONGO_URI')
app.config['JWT_SECRET_KEY'] = os.geten('JWT_SECRET_KEY')

# Initialize MongoDB, JWT, and rate limiter
mongo = PyMongo(app)
jwt = JWTManager(app)
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

from routes.auth_routes import auth_bp
from routes.note_routes import note_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(note_bp, url_prefix='/notes')

if __name__ == '__main__':
    app.run(port=3500, debug=True)
