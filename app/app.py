import os

from flask import Flask, render_template, request, redirect,send_from_directory
from flask.helpers import flash, url_for
from jinja2.exceptions import TemplateNotFound

from app.models import Earthquake,InjuredStatistics,HouseDamaged
from app.ext import db
from app.db import *
from app.custom.converter import RegexConverter

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
def mapPage():
    return render_template("index.html")


@app.route('/earthquakes')
def earthquakesListPage():
    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_earthquakes_num()
    earthquakes = get_earthquakes_data(limit=limit, offset=offset)

    return render_template("earthquakes.html", count=count, result=result, earthquakes=earthquakes, offset=offset,
                           limit=limit)


@app.route('/earthquakes/<int:id>', methods=['GET', 'PUT', 'DELETE', 'POST', 'DELETE'])
def earthquakesInfoPage(id):
    if request.method == 'GET':
        eq = Earthquake.query.get(id)
    # 房屋损害情况
    HoD = HouseDamaged.query.filter_by(EarthquakeId=id).all()
    # 人员伤亡情况
    IjS = InjuredStatistics.query.filter_by(EarthquakeId=id).all()
    # result = request.args.get("result", 'ALL', str)
    # offset = request.args.get('offset', 0, int)
    # limit = request.args.get('limit', 20, int)
    # count = get_earthquakes_num()
    # earthquakes = get_earthquakes_data(limit=limit, offset=offset)

    return render_template("earthquakeInfo.html", eq=eq, hoDs=HoD, ijSs=IjS)



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


@app.route('/docs', methods=['POST', 'GET'])
def getDocs():
    if request.method == 'POST':
        docName = request.values.get('docName')
        type = request.values.get('type')
        try:
            if type=="md" :
                print(docName)
                print(os.path.realpath(''))
                return send_from_directory('./doc/md',docName)
            else:
                return ""
        except TemplateNotFound as e:
            return "File Not Found"
    elif request.method == 'GET':
        return render_template("docs.html")



@app.route('/earthquakes/map')
def mainPage():
    return render_template("map.html")


@app.route('/baiduMap')
def baiduMapPage():
    data = {}
    data.update({"eqs":get_all_earthquakes_data()})
    return render_template("baidu.html",data=data)

@app.route('/baiduMap/<int:id>')
def earthMapPage(id):
    eq = None
    if request.method == 'GET':
        eq = Earthquake.query.get(id)
    data = {}
    data.update({"eqs":[eq]})
    return render_template("baidu.html",data=data)


@app.route('/disasters')
def disasterListPage():
    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_earthquakes_num()
    earthquakes = get_earthquakes_data(limit=limit, offset=offset)

    return render_template("disasters.html", count=count, result=result, earthquakes=earthquakes, offset=offset,
                           limit=limit)


@app.route('/injuredStatistics')
def InjuredStatisticsListPage():
    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_InjuredStatistics_num()
    injuredStatistics = get_all_InjuredStatistics_data(limit=limit, offset=offset)

    return render_template("InjuredStatistics.html", count=count, result=result, injuredStatistics=injuredStatistics, offset=offset,
                           limit=limit)


@app.route('/houseDamaged')
def HouseDamagedListPage():
    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_HouseDamaged_num()
    houseDamaged = get_all_HouseDamaged_data(limit=limit, offset=offset)

    return render_template("houseDamaged.html", count=count, result=result, houseDamaged=houseDamaged, offset=offset,
                           limit=limit)


@app.route('/test',methods=['POST','GET'])
def test():
    ## 测试

    return redirect(url_for("earthquakesListPage"))


if __name__ == '__main__':
    app.run(debug=True)
