from sqlalchemy.sql.expression import text
from flask import Blueprint, request, jsonify, stream_with_context

import json
from datetime import datetime
from typing import Dict

from sqlalchemy import desc, text
from werkzeug import Response

from app.ext import db
from app.models import Earthquake, Disaster, HouseDamaged, InjuredStatistics

api = Blueprint('api', __name__)
name_model_map = {
    'earthquakes': Earthquake,
    'disaster': Disaster,
    'houseDamaged': HouseDamaged,
    'InjuredStatistics': InjuredStatistics,
}


@api.route('/<string:table>/list', methods=['GET', 'PUT', 'DELETE', 'POST'])
def models(table: str):
    model = name_model_map[table]
    if request.method == 'GET':
        try:
            offset = request.args.get('offset', None, int)
            limit = request.args.get('limit', None, int)
            order_by = request.args.get("orderBy", "Id")
            order = request.args.get("order", "asc")
        except ValueError as e:
            return {""}
        if order_by != "":
            if order == "desc":
                data = model.query.order_by(desc(order_by))
            else:
                data = model.query.order_by(text(order_by))
        else:
            data = model.query
        eqs = data.limit(limit).offset(offset).all()
        res = {"limit": limit if limit else 0,
               "rows": [], "total": data.count()}
        for eq in eqs:
            res["rows"].append(to_dict(eq))
        return jsonify(res)
    elif request.method == "PUT":
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'POST':
        pass
    else:
        return '', 412


@api.route('/<string:table>/<int:id>',
           methods=['GET', 'PUT', 'DELETE', 'POST', "PATCH"])
def model(table, id):
    model = name_model_map[table]
    if request.method == 'GET':
        obj = model.query.filter(model.Id == id).first()
        type = request.args.get("type")
        if type:
            if type == "json":
                response = jsonify(to_dict(obj))
                response.headers.set("Content-Disposition", "attachment",
                                     filename=f"{model.__tablename__}_{id}.json")
                # 将 response 返回
                return response
            else:
                return "", 200
        else:
            return jsonify(to_dict(obj))
    elif request.method == "PUT":
        pass
    elif request.method == 'DELETE':
        db.session.delete(model.query.get(id))
        db.session.commit()
        return '', 204
    elif request.method == 'POST':
        pass
    elif request.method == "PATCH":
        row = model.query.get(id)
        if not row:
            return '', 404
        patch_dict = json.loads(request.data)
        for key, val in patch_dict.items():
            setattr(row, key, val)
        db.session.commit()
        return '', 200
    else:
        return '', 412


def to_dict(obj: object) -> Dict:
    d = {}
    for key, val in obj.__dict__.items():
        if type(val) in [str, int, float, datetime]:
            d[key] = val if type(val) != datetime else (
                val.strftime(r'%Y-%m-%d %H:%M:%S') if val else "")
    return d
