from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password):
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        try:
            self.client = MongoClient(
                HOST,
                PORT,
                username=username,
                password=password,
                authSource='admin'
            )

            self.database = self.client[DB]
            self.collection = self.database[COL]

        except PyMongoError as e:
            print("Connection failed:", e)

    def create(self, data):
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError as e:
                print("Insert failed:", e)
                return False
        else:
            print("No data provided to insert.")
            return False

    def read(self, query):
        if query is not None:
            try:
                data = self.collection.find(query)
                return list(data)
            except PyMongoError as e:
                print("Read failed:", e)
                return []
        else:
            print("No query provided.")
            return []

    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except PyMongoError as e:
                print("Update failed:", e)
                return 0
        else:
            print("Invalid query or update values.")
            return 0

    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError as e:
                print("Delete failed:", e)
                return 0
        else:
            print("No query provided.")
            return 0