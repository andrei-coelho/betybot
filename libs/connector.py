import mysql.connector 
import json

class Database(object):

    _instances = {}   
    _db = None

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(Database, class_).__new__(class_, *args, **kwargs)
            class_._instances[class_]._create()
        return class_._instances[class_]
    
    def _create(self):
      
        try:
            f = open("./acess.database.json", "r")
            j = json.loads(f.read())
            self._db = mysql.connector.connect(
                    host     = j['host'],
                    user     = j['user'],
                    password = j['password'],
                    database = j['db']
                )
        except:
            print("Erro ao tentar conectar com o banco de dados")

class Connector(Database):

    def __init__(self):
        super().__init__()
    
    def exec(self, query):
        try:
            cursor = self._db.cursor()
            cursor.execute(query)
            self._db.commit()
            return True
        except:
            return False

    def query(self, query):
        try:
            cursor = self._db.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
        except:
            return False