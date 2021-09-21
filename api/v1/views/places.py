#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from models import storage, place
from models.place import Place


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def place_all(city_id):
    """
    Retrieves a city object:
    """
    list = []
    for place in storage.all("Place").values():
        list.append(place.to_dict())
    return jsonify(list)


@app_views.route('/places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def plac_all(place_id):
    """
    Retrieves a place object:
    """
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict()), 200


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def place_delete(place_id):
    """
    Deletes a place object
    """
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def place_post(city_id):
    """
    Creates a Place
    """

    my_place = request.get_json()
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if "user_id" not in request.get_json().keys():
        abort(400, "Missing user_id")
    if "name" not in request.get_json().keys():
        abort(400, "Missing Missing name")
    else:
        my_place['city_id'] = city.id
        plaace = Place(**my_place)
        plaace.save()
        resp = jsonify(plaace.to_dict())
        return (resp), 201


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def place_put(place_id):
    """
    Updates a place object
    """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    pl = request.get_json()
    if pl is None:
        abort(400, "Not a JSON")
    else:
        for key, value in pl.items():
            if key in ['id'] and key in ['user_id'] and key in ['created_at']\
                    and key in ['city_id'] and key in ['updated_at']:
                pass
            else:
                setattr(place, key, value)
        storage.save()
        resp = user.to_dict()
        return jsonify(resp), 200