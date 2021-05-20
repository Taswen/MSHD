from flask import Flask, render_template,request
from ext import db
from db import *


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/settings.py")
    db.init_app(app)
    return app


app = create_app()


@app.route('/')
def earthquakesListPage():


    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_earthquakes_num()
    earthquakes = get_earthquakes_data(limit=limit,offset=offset)


    return render_template("index.html",count=count, result=result, earthquakes=earthquakes,offset=offset,limit = limit)




if __name__ == '__main__':
    app.run(debug=True)
