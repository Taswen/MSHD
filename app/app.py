from flask import Flask, render_template, request, redirect
from flask.helpers import flash, url_for
from app.ext import db
from app.db import get_earthquakes_num,get_earthquakes_data
import os



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/settings.py")
    db.init_app(app)
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


@app.route('/uplloader', methods=['POST', 'GET'])
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
