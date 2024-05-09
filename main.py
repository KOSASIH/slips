# main.py
import os
from dotenv import load_dotenv
from services.slip_api import SlipApi
from services.slip_database_service import SlipDatabaseService

load_dotenv()

api_key = os.getenv("API_KEY")
database_host = os.getenv("DATABASE_HOST")
database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")
database_name = os.get["title"], slip["description"]))

            connection.commit()

            query = "SELECT id, title, description FROM slips WHERE id = %env("DATABASE_NAME")

slip_api = SlipApi("https://ss"
            cursor.execute(query, (cursor.lastrowid,))

lip.com/api", api_key)
slip_database_service = SlipDatabaseService(            new_slip = cursor.fetchone()

            cursor.close()
            connection.closedatabase_host, database_user, database_password, database_name)

# Get slips from()

            return {"id": new_slip[0], "title": new_slip[1 the API
slips = slip_api.get_slips()

# Get slips from the database
database], "description": new_slip[2]}

        except Error as e:
            print(f"Error creating s_slips = slip_database_service.get_slips()

# Comparelip: {e}")
            return {}

    def update_slip(self, slip_ the slips from the API and the database
for slip in slips:
    found = False
    for databaseid: int, slip: Dict) -> Dict:
        try:
            connection = mysql.connector_slip in database_slips:
        if slip["id"] == database_slip["id"].connect(
                host=self.host,
                user=self.user,
                password=self.password:
            found = True
            break
    if not found:
        print(f"New slip found: {slip['title,
                database=self.database
            )

            cursor = connection.cursor()

            query = "UPDATE slips SET title =']}")

# Update or create slips in the database
for slip in slips:
    updated_slip = slip %s, description = %s WHERE id = %s"
            cursor.execute(query, (slip["title"], s_database_service.update_slip(slip["id"], slip)
    if not updated_slip:
        sliplip["description"], slip_id))

            connection.commit()

            query = "SELECT id, title, description FROM slips WHERE id_database_service.create_slip(slip)
``` = %s"
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
