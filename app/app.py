from flask import Flask, render_template
from app.ext import db
from app.db import get_data


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    db.init_app(app)
    return app


app = create_app()


@app.route('/')
def hello_world():
    earthquakes = get_data()
    return render_template("index.html", earthquakes=earthquakes)




if __name__ == '__main__':
    app.run(debug=True)
