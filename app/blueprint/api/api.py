# -*- coding: utf-8 -*-
# filename api.py
from crypt import methods
from flask import Blueprint,render_template, request
from app.db import *

api = Blueprint('api',__name__)

@api.route('/earthquakes', methods=['GET', 'PUT', 'DELETE', 'POST'])
def earthquakes():
    if request.method == 'GET':
        try:
            offset = request.args.get('offset', None, int)
            limit = request.args.get('limit', None, int)
            s = request.args.get("orderBy")
            s = request.args.get("order")
            s = request.args.get("orderBy")
            s = request.args.get("order")
        except ValueError as e :
            return {""}
        # if()
        # Earthquake.query.order_by(text("id")).limit(limit).offset(offset).all()



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