from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize the database
db = SQLAlchemy(app)

# Initialize JWT authentication
jwt = JWTManager(app)

# Enable CORS
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)