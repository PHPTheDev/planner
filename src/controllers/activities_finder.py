from typing import Dict

class Activitiesfinder:
    def __init__(self, __Activitiesrepository) -> None:
        self.__activities_repository = __Activitiesrepository

    def find_from_trip(self, trip_id) -> Dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)

            formatted_activities = []
            for activity in activities:
                formatted_activities.append({
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": activity[3]
                })
            
            return {
                "body": { "activities": formatted_activities },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }