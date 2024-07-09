from typing import Dict

class Tripconfirmer:
    def __init__(self, trips_repository) -> None:
        self.__trip_repository = trips_repository

    def confirm(self, trip_id) -> Dict:
        try:
            self.__trip_repository.update_trip_status(trip_id)
            return {
                "body": None,
                "status_code": 204
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad request", "message": exception},
                "status_code": 400
            }