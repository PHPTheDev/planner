from typing import Dict
from src.drivers.email_sender import send_email
import uuid

class Tripcreator:
    def __init__(self, __Triprepository, __Emailsrepository) -> None:
        self.__trip_repository = __Triprepository
        self.__email_repository = __Emailsrepository

    def create(self, body) -> Dict:
        try:
            emails = body.get('emails_to_invite')
            trip_id = str(uuid.uuid4())
            trip_infos = {
                **body, "id": trip_id
            }

            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__email_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })
            send_email([body["owner_email"]],
                       f"http://localhost:3000/trips/{trip_id}/confirm")
            return {
                "body": {"id": trip_id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad request", "message": exception},
                "status_code": 400
            }