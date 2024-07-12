from typing import Dict

class Participantconfirmer:
    def __init__(self, Participantsrepository) -> None:
        self.__participants_repository = Participantsrepository

    def confirm(self, trip_id) -> Dict:
        try:
            self.__participants_repository.confirm_participant(trip_id)
            return { "body": None, "status_code": 204 }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }