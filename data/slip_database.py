# data/slip_database.py
import sqlite3
from typing import List, Dict

class SlipDatabase:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS slips (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL
            )
        """)

        self.conn.commit()

    def insert_slip(self, slip: Dict) -> None:
        self.cursor.execute("""
            INSERT INTO slips (title, description)
            VALUES (?, ?)
        """, (slip["title"], slip["description"]))

        self.conn.commit()

    def update_slip(self, slip: Dict) -> None:
        self.cursor.execute("""
            UPDATE slips
            SET title = ?, description = ?
            WHERE id = ?
        """, (slip["title"], slip["description"], slip["id"]))

        self.conn.commit()

    def delete_slip(self, slip_id: int) -> None:
        self.cursor.execute("""
            DELETE FROM slips
            WHERE id = ?
        """, (slip_id,))

        self.conn.commit()

    def get_slip(self, slip_id: int) -> Dict:
        self.cursor.execute("""
            SELECT id, title, description
            FROM slips
            WHERE id = ?
        """, (slip_id,))

        slip = self.cursor.fetchone()

        if slip:
            return {"id": slip[0], "title": slip[1], "description": slip[2]}
        else:
            return None

    def get_slips(self) -> List[Dict]:
        self.cursor.execute("""
            SELECT id, title, description
            FROM slips
        """)

        slips = self.cursor.fetchall()

        return [{"id": slip[0], "title": slip[1], "description": slip[2]} for slip in slips]

    def close(self) -> None:
        self.conn.close()
