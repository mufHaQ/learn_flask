from flask import Flask, render_template, flash, session
from dotenv import load_dotenv
from datetime import timedelta
import os


# load .env
load_dotenv()


app = Flask(__name__, template_folder='src/templates',
            static_folder='src/static', static_url_path='/assets')
app.secret_key = os.getenv('SECRET_KEY')
app.permanent_session_lifetime = timedelta(days=30)


@app.route('/')
def home():
    return render_template('pages/home.html')


# if using python3 or python comman to run
if __name__ == '__main__':
    APP_PORT = os.getenv('FLASK_RUN_PORT')
    app.run(debug=True, port=APP_PORT)
