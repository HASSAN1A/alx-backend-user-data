#!/usr/bin/env python3
""" module docs """
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ method docs """
    return jsonify({"status": "OK"})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ method docs """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ method docs """
    abort(403)


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ method docs """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
