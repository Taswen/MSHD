from sqlalchemy.sql.expression import text
from app.models import Earthquake
from flask import Blueprint, request, jsonify
from sqlalchemy import desc
from app.db import db

api = Blueprint('api', __name__)


@api.route('/earthquakes/', methods=['GET', 'PUT', 'DELETE', 'POST'])
def earthquakes():
    if request.method == 'GET':
        try:
            offset = request.args.get('offset', None, int)
            limit = request.args.get('limit', None, int)
            orderBy = request.args.get("orderBy")
            order = request.args.get("order")
        except ValueError:
            return {""}
        if orderBy != "":
            if order == "desc":
                datas = Earthquake.query.order_by(desc(orderBy))
            else:
                datas = Earthquake.query.order_by(text(orderBy))
        else:
            datas = Earthquake.query
        eqs = datas.limit(limit).offset(offset).all()
        res = {
            "limit": limit if limit != None else 0,
            "rows": [], "total": datas.count()
        }
        for eq in eqs:
            res["rows"].append(eq.toMap())
        return jsonify(res)
    elif request.method == "PUT":
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'POST':
        pass
    else:
        return '', 412


@api.route('/earthquakes/<id>',
           methods=['GET', 'PUT', 'DELETE', 'POST', "PATCH"])
def earthquake(id):
    if request.method == 'GET':
        pass
    elif request.method == "PUT":
        pass
    elif request.method == 'DELETE':
        db.session.delete(Earthquake.query.get(id))
        db.session.commit()
        return '', 204
    elif request.method == 'POST':
        pass
    elif request.method == "PATCH":
        pass
    else:
        return '', 412
