from flask import jsonify, Blueprint, request
trips_routes_bp = Blueprint("trip_routes", __name__)

from src.controllers.trip_creator import Tripcreator
from src.controllers.trip_finder import Tripfinder
from src.controllers.trip_confirmer import Tripconfirmer
from src.controllers.link_creator import Linkcreator
from src.controllers.link_finder import LinkFinder

from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository


from src.models.settings.db_connection_handler import db_connection_handler


@trips_routes_bp.route("/trips", methods=["POST"])

def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = Tripcreator(trips_repository, emails_repository)


    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])

def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = Tripfinder(trips_repository)

    response = controller.find_trip_details(tripId)
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])    

def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = Tripconfirmer(trips_repository)

    response = controller.confirm(tripId)
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"]) 

def link_creator(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = Linkcreator(links_repository)

    response = controller.create_link(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"]) 

def link_finder(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)

    response = controller.find(tripId)
    return jsonify(response["body"]), response["status_code"]
