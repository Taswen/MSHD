from app.models import Earthquake
from flask import Flask, render_template, request, redirect
from flask.helpers import flash, url_for
from app.ext import db
from app.db import get_earthquakes_num,get_earthquakes_data
from app.custom.converter import RegexConverter
import os

# from scanner.scanner import Scanner


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/settings.py")
    app.url_map.converters['regex']=RegexConverter
    db.init_app(app)
    # Scanner(app).run()
    return app


app = create_app()


@app.route('/')
@app.route('/earthquakes')
def earthquakesListPage():
    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_earthquakes_num()
    earthquakes = get_earthquakes_data(limit=limit, offset=offset)

    return render_template("earthquakes.html", count=count, result=result, earthquakes=earthquakes, offset=offset,
                           limit=limit)

@app.route('/earthquakes/<int:id>', methods=['GET','PUT', 'DELETE', 'POST', 'DELETE'])
def earthquakesInfoPage(id):
    if request.method == 'GET':
        eq = Earthquake.query.get(id)

    
    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_earthquakes_num()
    earthquakes = get_earthquakes_data(limit=limit, offset=offset)

    return render_template("earthquakes.html", count=count, result=result, earthquakes=earthquakes, offset=offset,
                           limit=limit)


@app.route('/uploader', methods=['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        pass
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        flash('file uploaded successfully')
    else:
        pass
    return redirect(url_for("earthquakesListPage"))


@app.route('/test',methods=['POST','GET'])
def test():
    ## 测试

    return redirect(url_for("earthquakesListPage"))


if __name__ == '__main__':
    app.run(debug=True)
