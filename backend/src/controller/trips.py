from flask import request
from flask_restx import Namespace, Resource, fields

from src.controller.auth import token_required
from ..model.trip import Trip
from ..model.user import User

trips_api = Namespace("trips", "Trips API", path="/trips")

create_trip_model = trips_api.model(
    "CreateTripModel",
    {
        "name": fields.String(required=True, min_length=1, max_length=64),
        "startDate": fields.Date(required=True),
        "endDate": fields.Date(required=True),
        "description": fields.String(required=True),
    },
)


@trips_api.route("/")
class Trips(Resource):
    """
    Create trip
    """

    @trips_api.expect(create_trip_model, validate=True)
    @token_required
    def post(self, current_user_auth):
        try:
            body = request.get_json()
            _name = body.get("name")
            _start_date = body.get("startDate")
            _end_date = body.get("endDate")
            _description = body.get("description")

            new_trip = Trip(
                name=_name,
                start_date=_start_date,
                end_date=_end_date,
                description=_description,
            )

            current_user = User.get_by_id(current_user_auth.user_id)
            current_user.trips.append(new_trip)
            current_user.save()

            trips = [trip.toJSON() for trip in current_user.get_trips()[::-1]]
            return {"success": True, "trips": trips}, 200

        except:
            return {"success": False, "msg": "Trip was unable to be created."}, 400

    @token_required
    def get(self, current_user_auth):
        try:
            current_user = User.get_by_id(current_user_auth.user_id)

            trips = [trip.toJSON() for trip in current_user.get_trips()[::-1]]
            return {"success": True, "trips": trips}, 200

        except:
            return {"success": False, "msg": "Unable to retrieve trips."}, 400


update_trip_model = trips_api.model(
    "CreateTripModel",
    {
        "name": fields.String(min_length=1, max_length=64),
        "startDate": fields.Date(),
        "endDate": fields.Date(),
        "description": fields.String(),
    },
)


@trips_api.route("/<string:trip_uuid>")
class IndividualTrips(Resource):
    """
    Update trip
    """

    @trips_api.expect(update_trip_model, validate=True)
    @token_required
    def put(self, current_user_auth, trip_uuid):
        try:
            body = request.get_json()
            curr_trip = Trip.get_by_uuid(trip_uuid)
            if not curr_trip or not curr_trip.contains_user(current_user_auth.user_id):
                return {"success": False, "msg": "Trip not found."}, 400

            curr_trip.update(body)
            curr_trip.save()

            current_user = User.get_by_id(current_user_auth.user_id)
            trips = [trip.toJSON() for trip in current_user.get_trips()]
            return {"success": True, "trips": trips}, 200
        except:
            return {"success": False, "msg": "Unable to update trip."}, 400

    """
    Delete trip
    """

    @token_required
    def delete(self, current_user_auth, trip_uuid):
        try:
            curr_trip = Trip.get_by_uuid(trip_uuid)
            if not curr_trip or not curr_trip.contains_user(current_user_auth.user_id):
                return {"success": False, "msg": "Trip not found."}, 400
            curr_trip.delete()

            current_user = User.get_by_id(current_user_auth.user_id)
            trips = [trip.toJSON() for trip in current_user.get_trips()]
            return {"success": True, "trips": trips}, 200

        except:
            return {"success": False, "msg": "Unable to delete trip."}, 400


add_users_model = trips_api.model(
    "AddUsersModel",
    {
        "users": fields.List(fields.String(), required=True),  # emails of users
    },
)


@trips_api.route("/<string:trip_uuid>/users")
class TripUsers(Resource):
    """
    Retrieve trip's users
    """

    @token_required
    def get(self, current_user_auth, trip_uuid):
        try:
            curr_trip = Trip.get_by_uuid(trip_uuid)
            if not curr_trip or not curr_trip.contains_user(current_user_auth.user_id):
                return {"success": False, "msg": "Trip not found."}, 400

            users = [user.toJSON() for user in curr_trip.users]
            return {"success": True, "users": users}, 200

        except:
            return {"success": False, "msg": "Unable to retrieve trip users."}, 400

    """
    Add trip's users
    """

    @trips_api.expect(add_users_model, validate=True)
    @token_required
    def put(self, current_user_auth, trip_uuid):
        try:
            curr_trip = Trip.get_by_uuid(trip_uuid)
            if not curr_trip or not curr_trip.contains_user(current_user_auth.user_id):
                return {"success": False, "msg": "Trip not found."}, 400
            body = request.get_json()

            users = []
            for email in body.get("users"):
                curr_user = User.get_by_email(email)
                if not curr_user:
                    return {"success": False, "msg": "User not found."}, 400
                users.append(curr_user)
            curr_trip.users = users
            curr_trip.save()

            users = [user.toJSON() for user in curr_trip.users]
            return {"success": True, "users": users}, 200

        except:
            return {"success": False, "msg": "Unable to update trip users."}, 400
