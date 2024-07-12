from typing import Dict
import uuid

class Activitycreator:
    def __init__(self, __Activityrepository) -> None:
        self.__activity_repository = __Activityrepository

    def create_activity(self, body, trip_id) -> Dict:
        try:
            id = str(uuid.uuid4()) 
            activities_infos = {
                    "id": id,
                    "trip_id": trip_id,
                    "title": body["title"],
                    "occurs_at": body["occurs_at"],
            }         

            self.__activity_repository.registry_activities(activities_infos)

            return {
                "body": {"activity_id": id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad request", "message": exception},
                "status_code": 400
            }