from typing import Dict
import uuid

class Participantcreator:
    def __init__(self, __Particpantrepository, __Emailrepository) -> None:
        self.__participants_repository = __Particpantrepository
        self.__email_repository = __Emailrepository

    def create_participant(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4()) 
            email_id = str(uuid.uuid4())

            email_infos = {
                "email": body["email"],
                "id": email_id,
                "trip_id": trip_id
            }
            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"]
            }            

            self.__email_repository.registry_email(email_infos)
            self.__participants_repository.registry_participants(participant_infos)

            return {
                "body": {"participant_id": participant_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad request", "message": exception},
                "status_code": 400
            }