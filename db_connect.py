import sqlite3 as db


class DataBaseControl:

    def __init__(self):
        self.connection = db.connect("data/user_data.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS Data(
        Checked BOOL,
        Text VARCHAR(100) UNIQUE);
        """)

    def insert_data(self, text):
        self.cursor.executescript(f"INSERT INTO Data VALUES (FALSE, '{text}');")
        self.connection.commit()

    def update_data(self, text, p_text):
        print("update ", text, p_text)
        self.cursor.executescript(f"UPDATE Data SET Text='{text}' WHERE Text='{p_text}'")
        self.connection.commit()

    def delete_data(self, text):
        self.cursor.executescript(f"DELETE FROM Data WHERE Text='{text}'")
        self.connection.commit()

    def return_data(self):
        res = self.cursor.execute("SELECT Checked, Text FROM Data")
        return res.fetchall()

    def save_check(self, checked, text):
        self.cursor.execute(f"UPDATE Data SET Checked={checked} WHERE Text='{text}'")
        self.connection.commit()


