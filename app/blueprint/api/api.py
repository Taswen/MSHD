# -*- coding: utf-8 -*-
# filename api.py
from flask import Blueprint,render_template, request,jsonify
from app.db import *

api = Blueprint('api',__name__)

@api.route('/earthquakes/', methods=['GET', 'PUT', 'DELETE', 'POST'])
def earthquakes():
    if request.method == 'GET':
        try:
            offset = request.args.get('offset', None, int)
            limit = request.args.get('limit', None, int)
            orderBy = request.args.get("orderBy")
            order = request.args.get("order")
        except ValueError as e :
            return {""}
        # if()
        datas = Earthquake.query.order_by(text("id"))
        eqs=  datas.limit(limit).offset(offset).all()
        res = {"limit":limit if limit!= None else 0 ,"rows":[],"total":datas.count()}
        for eq in eqs:
            res["rows"].append(eq.toMap())
        print(res)
        return jsonify(res)
    elif request.method == "PUT":
        pass 
    elif request.method == 'DELETE':
        pass
    elif request.method == 'POST':
        pass
    else:
        return '',412

@api.route('/earthquakes/<id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def earthquake(id):
    if request.method == 'GET':
        pass
    elif request.method == "PUT":
        pass 
    elif request.method == 'DELETE':
        pass
    elif request.method == 'POST':
        pass
    else:
        return '',412