from sqlite3 import Connection
from typing import Dict, Tuple, List

class Activiesrepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def registry_activities(self, activity_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO activities (id, trip_id, title, occurs_at) VALUES (?,?,?,?)
            ''', (
                    activity_infos["id"],
                    activity_infos["trip_id"],
                    activity_infos["title"],
                    activity_infos["occurs_at"],
                )
        )
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM activities WHERE trip_id = ? 
            ''', (trip_id,)
        )
        activities = cursor.fetchall()
        return activities
    
    def confirm_participant(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            UPDATE participants SET is_confirmed = 1 WHERE id = ?
            ''', (participant_id,)
        )
        self.__conn.commit()
