from flask import Flask, render_template,request,redirect
from flask.helpers import flash, url_for
from app.ext import db
from app.db import *
import os

############# INIT ##############
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/settings.py")
    db.init_app(app)
    return app

app = create_app()

############# ROUTE ##############
@app.route('/')
def earthquakesListPage():

    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_earthquakes_num()
    earthquakes = get_earthquakes_data(limit=limit,offset=offset)

    return render_template("index.html",count=count, result=result, earthquakes=earthquakes,offset=offset,limit = limit)

@app.route('/uploader',methods=['POST','GET'])
def uploader():
    if request.method == 'POST':
        print("IN")
        f = request.files['file']
        print(os.path)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))        
        flash('file uploaded successfully')
    else:
        print("IN GET")
    return redirect(url_for("earthquakesListPage"))


@app.route('/test',methods=['POST','GET'])
def test():
    ## 测试

    return redirect(url_for("earthquakesListPage"))


#############  ##############
if __name__ == '__main__':
    app.run(debug=True)
