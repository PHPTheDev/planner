from typing import Dict

class Tripfinder:
    def __init__(self, Tripsrepository) -> None:
        self.__trips_repository = Tripsrepository

    def find_trip_details(self, trip_id) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)    
            if not trip: raise Exception("No trip found")
            return {
                    "body": {
                        "trip":{
                            "id": trip[0],
                            "destination":trip[1],
                            "start_at":trip[2],
                            "end_at":trip[3],
                            "status":trip[6],
                        }
                    }, "status_code": 201
                }
        except Exception as exception:
            return {
                "body": {"error": "Bad request", "message": exception},
                "status_code": 400
            }