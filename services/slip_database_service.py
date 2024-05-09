# services/slip_database_service.py
import mysql.connector
from mysql.connector import Error
from typing import List, Dict

class SlipDatabaseService:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_slips(self) -> List[Dict]:
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            cursor = connection.cursor()

            query = "SELECT id, title, description FROM slips"
            cursor.execute(query)

            slips = []
            for (id, title, description) in cursor:
                slip = {"id": id, "title": title, "description": description}
                slips.append(slip)

            cursor.close()
            connection.close()

            return slips

        except Error as e:
            print(f"Error fetching slips: {e}")
            return []

    def create_slip(self, slip: Dict) -> Dict:
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            cursor = connection.cursor()

            query = "INSERT INTO slips (title, description) VALUES (%s, %s)"
            cursor.execute(query, (slip["title"], slip["description"]))

            connection.commit()

            query = "SELECT id, title, description FROM slips WHERE id = %s"
            cursor.execute(query, (cursor.lastrowid,))

            new_slip = cursor.fetchone()

            cursor.close()
            connection.close()

            return {"id": new_slip[0], "title": new_slip[1], "description": new_slip[2]}

        except Error as e:
            print(f"Error creating slip: {e}")
            return {}

    def update_slip(self, slip_id: int, slip: Dict) -> Dict:
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            cursor = connection.cursor()

            query = "UPDATE slips SET title = %s, description = %s WHERE id = %s"
            cursor.execute(query, (slip["title"], slip["description"], slip_id))

            connection.commit()

            query = "SELECT id, title, description FROM slips WHERE id = %s"
            cursor.execute(query, (slip_id,))

            updated_slip = cursor.fetchone()

            cursor.close()
            connection.close()

            return {"id": updated_slip[0], "title": updated_slip[1], "description": updated_slip[2]}

        except Error as e:
            print(f"Error updating slip: {e}")
            return {}

    def delete_slip(self, slip_id: int) -> None:
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            cursor = connection.cursor()

            query = "DELETE FROM slips WHERE id = %s"
            cursor.execute(query, (slip_id,))

            connection.commit()

            cursor.close()
            connection.close()

        except Error as e:
            print(f"Error deleting slip: {e}")
