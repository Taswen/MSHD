import os
from flask import  render_template, request, redirect,send_from_directory
from flask.helpers import flash, url_for
from jinja2.exceptions import TemplateNotFound

from app import create_app
from app.models import Earthquake,InjuredStatistics,HouseDamaged
from app.db import *



app = create_app("development")



@app.errorhandler(404)
def Not_FOUND_404(e):
    return render_template('error/404.html'),404



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


@app.route('/earthquakes/<int:id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
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



@app.route('/upload', methods=['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        if not request.data is None:
            print("Not QE")
            return redirect(url_for("mainPage"))
        print(type(request.date))
        # f = request.files['file']
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        # flash('file uploaded successfully')
    else:
        print("GET")
        pass
    print("OUT ")
    # return redirect(url_for("earthquakesListPage"))


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

    return  render_template("indexP.html")


if __name__ == '__main__':
    app.run(debug=True)
