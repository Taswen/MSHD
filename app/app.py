from app.db import get_InjuredStatistics_num, get_all_HouseDamaged_data
from app.db import get_earthquakes_num, get_all_earthquakes_data
from app.db import get_earthquakes_data, get_HouseDamaged_num
from app.db import get_HouseDamaged_num
from app.db import get_all_InjuredStatistics_data
from app.models import Earthquake, HouseDamaged, InjuredStatistics
import hashlib
import os
import time

from flask import render_template, request, send_from_directory, jsonify
from jinja2.exceptions import TemplateNotFound

from app import create_app
from app.blueprint.api.api import api

app = create_app("development")

app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def mapPage():
    return render_template("index.html")


@app.route('/earthquakes')
def earthquakesListPage():
    count = get_earthquakes_num()
    return render_template("earthquakes.html", count=count)


@app.route('/earthquakes/<int:id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def earthquakesInfoPage(id):
    if request.method == 'GET':
        eq = Earthquake.query.get(id)
    # 房屋损害情况
    HoD = HouseDamaged.query.filter_by(EarthquakeId=id).all()
    # 人员伤亡情况
    IjS = InjuredStatistics.query.filter_by(EarthquakeId=id).all()

    return render_template("earthquakeInfo.html", eq=eq, hoDs=HoD, ijSs=IjS)


@app.route('/houseDamaged/<int:id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def houseDamagedInfoPage(id):
    if request.method == 'GET':
        hd = HouseDamaged.query.get(id)
    # 编码

    # 房屋损害情况
    eqs = Earthquake.query.filter_by(Id=hd.EarthquakeId).all()
    # 人员伤亡情况
    # IjS = InjuredStatistics.query.filter_by(EarthquakeId=id).all()

    return render_template("houseDamagedInfo.html", hd=hd, eqs=eqs)


@app.route('/docs', methods=['POST', 'GET'])
def getDocs():
    if request.method == 'POST':
        docName = request.values.get('docName')
        type = request.values.get('type')
        try:
            if type == "md":
                print(docName)
                print(os.path.realpath(''))
                return send_from_directory('./doc/md', docName)
            else:
                return ""
        except TemplateNotFound:
            return "File Not Found"
    elif request.method == 'GET':
        return render_template("docs.html")


@app.route('/earthquakes/map')
def mainPage():
    return render_template("map.html")


@app.route('/baiduMap')
def baiduMapPage():
    data = {}
    data.update({"eqs": get_all_earthquakes_data()})
    return render_template("baidu.html", data=data)


@app.route('/baiduMap/<int:id>')
def earthMapPage(id):
    eq = None
    if request.method == 'GET':
        eq = Earthquake.query.get(id)
    data = {}
    data.update({"eqs": [eq]})
    return render_template("baidu.html", data=data)


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
    injuredStatistics = get_all_InjuredStatistics_data(
        limit=limit, offset=offset)

    return render_template("InjuredStatistics.html", count=count, result=result, injuredStatistics=injuredStatistics,
                           offset=offset,
                           limit=limit)


@app.route('/injuredStatistics/<int:id>', methods=['GET', 'PUT', 'DELETE', 'POST', 'DELETE'])
def injuredStatisticsInfoPage(id):
    if request.method == 'GET':
        ij = InjuredStatistics.query.get(id)
    return render_template("InjuredStatisticsInfo.html", ij=ij)


@app.route('/houseDamaged')
def house_damaged_list_page():
    result = request.args.get("result", 'ALL', str)
    offset = request.args.get('offset', 0, int)
    limit = request.args.get('limit', 20, int)
    count = get_HouseDamaged_num()
    houseDamaged = get_all_HouseDamaged_data(limit=limit, offset=offset)

    return render_template("houseDamaged.html", count=count, result=result, houseDamaged=houseDamaged, offset=offset,
                           limit=limit)


@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('file_uploader')
    for file in files:
        ext = file.filename.rsplit('.')[-1]
        filename = hashlib.md5(str(time.time()).encode(
            'utf-8')).hexdigest()[:15] + ext
        # filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'msg': 'upload success'})


if __name__ == '__main__':
    app.run(debug=True)
