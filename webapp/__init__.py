from flask import Flask, render_template
# from webapp.python_org_news import get_python_news
from webapp.forms import LoginForm
# from webapp.weather import weather_by_city
from webapp.model import db, User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def login():
        title = "Вход в базу договоров"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app