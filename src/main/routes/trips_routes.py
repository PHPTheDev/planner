from flask import jsonify, Blueprint, request
trips_routes_bp = Blueprint("trip_routes", __name__)

from src.controllers.trip_creator import Tripcreator
from src.controllers.trip_finder import Tripfinder
from src.controllers.trip_confirmer import Tripconfirmer

from src.controllers.link_creator import Linkcreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participants_creator import Participantcreator
from src.controllers.participant_finder import Participantfinder
from src.controllers.participant_confirmer import Participantconfirmer

from src.controllers.activities_creator import Activitycreator
from src.controllers.activities_finder import Activitiesfinder

from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import Participantsrepository
from src.models.repositories.activities_repository import Activiesrepository


from src.models.settings.db_connection_handler import db_connection_handler


# ----------------------------------------------- Criar viagem

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = Tripcreator(trips_repository, emails_repository)


    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]

# ----------------------------------------------- Achar viagem

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = Tripfinder(trips_repository)

    response = controller.find_trip_details(tripId)
    return jsonify(response["body"]), response["status_code"]

# ----------------------------------------------- Confirmar viagem

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])    
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = Tripconfirmer(trips_repository)

    response = controller.confirm(tripId)
    return jsonify(response["body"]), response["status_code"]

# ----------------------------------------------- Criar link

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"]) 
def link_creator(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = Linkcreator(links_repository)

    response = controller.create_link(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]

# ----------------------------------------------- Achar link

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"]) 
def link_finder(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)

    response = controller.find(tripId)
    return jsonify(response["body"]), response["status_code"]

# ----------------------------------------------- Criar participante

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"]) 
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    participant_repository = Participantsrepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = Participantcreator(participant_repository, emails_repository)

    response = controller.create_participant(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]


# ----------------------------------------------- Criar atividade

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"]) 
def activities_creator(tripId):
    conn = db_connection_handler.get_connection()
    activity_repository = Activiesrepository(conn)
    controller = Activitycreator(activity_repository)

    response = controller.create_activity(request.json, tripId)
    return jsonify(response["body"]), response["status_code"]

# ----------------------------------------------- Achar participante

@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = Participantsrepository(conn)
    controller = Participantfinder(participants_repository)

    response = controller.find_participants_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]

# ----------------------------------------------- Achar atividade

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = Activiesrepository(conn)
    controller = Activitiesfinder(activities_repository)

    response = controller.find_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]

# ----------------------------------------------- Confirmar participante

@trips_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participants_repository = Participantsrepository(conn)
    controller = Participantconfirmer(participants_repository)

    response = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]
