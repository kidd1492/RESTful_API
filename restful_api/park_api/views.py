from flask import Blueprint, render_template, request, jsonify, redirect, session
from . import db
from .models import Park, Camp, User
from functools import wraps
from .helper import apology, api_creation

views = Blueprint('views', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        user = db.session.query(User).filter_by(api_key=token).first()

        if not user:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(user, *args, **kwargs)

    return decorated


'''API URI I added the version to the uri
   /api/v1/parks will list all parks'''

@views.route('/api/v1/parks')
@token_required
def api_parks():
    start = request.args.get('start', default=0, type=int)
    limit = request.args.get('limit', default=25, type=int)
    parks = db.session.query(Park).offset(start).limit(limit).all()
    
    # Convert the query results to a list of dictionaries
    parks_list = []
    for park in parks:
        park_dict = {
            'park_id': park.park_id,
            'park_code': park.park_code,
            'name': park.name,
            'description': park.description,
            'url': park.url
        }
        parks_list.append(park_dict)

    # Return the list as a JSON response
    return jsonify({"data": parks_list})


''' api route for individual park'''
@views.route('/api/v1/parks/<int:park_id>')
def park_details(park_id):
    park = db.session.query(Park).filter_by(park_id=park_id).first()

    if park:
        park_detail = {
            'park_id': park.park_id,
            'park_code': park.park_code,
            'name': park.name,
            'description': park.description,
            'url': park.url
        }
        return jsonify({'data': park_detail})
    else:
        return jsonify({'error': "Park not found"}), 404


''' I need to set a limit and an offset=start'''
@views.route('/api/v1/camps')
def api_camps():
    start = request.args.get('start', default=0, type=int)
    limit = request.args.get('limit', default=50, type=int)
    camps = db.session.query(Camp).offset(start).limit(limit).all()

    camps_list = []
    for camp in camps:
        camp_dict = {
            'id': camp.id,
            'name': camp.name,
            'park_code': camp.park_code,
            'state': camp.state,
            'longitude': camp.longitude,
            'latitude': camp.latitude,
            'totalSites': camp.totalSites,
            'tentOnly': camp.tentOnly,
            'electricalHookups': camp.electricalHookups,
            'showers': camp.showers,
            'dumpStation': camp.dumpStation,
            'host': camp.host,
            'potableWater': camp.potableWater,
            'firewoodForSale': camp.firewoodForSale,
            'reservationUrl': camp.reservationUrl
        }
        camps_list.append(camp_dict)

    # Return the list of camps as a JSON response
    return jsonify({'data': camps_list})



@views.route('/api/v1/camps/<int:id>')
def camp_details(id):
    camp = db.session.query(Camp).filter_by(id=id).first()

    if camp:
        camp_detail = {
            'id': camp.id,
            'name': camp.name,
            'park_code': camp.park_code,
            'state': camp.state,
            'longitude': camp.longitude,
            'latitude': camp.latitude,
            'totalSites': camp.totalSites,
            'tentOnly': camp.tentOnly,
            'electricalHookups': camp.electricalHookups,
            'showers': camp.showers,
            'dumpStation': camp.dumpStation,
            'host': camp.host,
            'potableWater': camp.potableWater,
            'firewoodForSale': camp.firewoodForSale,
            'reservationUrl': camp.reservationUrl
        }
        return jsonify({'data': camp_detail})
    else:
        return jsonify({'error': "Park not found"}), 404
    

'''GET /camps?state={state} - Retrieves camps filtered by state.'''
@views.route('/api/v1/camps/<string:state>')
def state_camp(state):
    camps = db.session.query(Camp).filter_by(state=state).all()

    camps_list = []
    for camp in camps:
        # Serialize the camp data into a dictionary
        camp_dict = {
            'id': camp.id,
            'name': camp.name,
            'park_code': camp.park_code,
            'state': camp.state,
            'longitude': camp.longitude,
            'latitude': camp.latitude,
            'totalSites': camp.totalSites,
            'tentOnly': camp.tentOnly,
            'electricalHookups': camp.electricalHookups,
            'showers': camp.showers,
            'dumpStation': camp.dumpStation,
            'host': camp.host,
            'potableWater': camp.potableWater,
            'firewoodForSale': camp.firewoodForSale,
            'reservationUrl': camp.reservationUrl
        }
        camps_list.append(camp_dict)

    # Return the list of camps as a JSON response
    return jsonify({'data': camps_list})