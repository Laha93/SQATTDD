from flask import Flask
from app.routes import bp  # Import your routes blueprint

app = Flask(__name__)
app.register_blueprint(bp)  # Register the blueprint with your app

if __name__ == '__main__':
    app.run(debug=True)
