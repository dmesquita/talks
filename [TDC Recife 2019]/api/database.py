import sqlite3

class Database(object):

    def save(self, params):
        self._conn = sqlite3.connect('my_database.sqlite')
        self._cursor = self._conn.cursor()
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS requests (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, model_version TEXT)''')
        result = self._cursor.execute("INSERT INTO requests (title,description, model_version) VALUES (?,?,?)", params)
        self._conn.commit()
        self._conn.close()
        return result
