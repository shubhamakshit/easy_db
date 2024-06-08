from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from DataObject import DataObject
from uuid import uuid4

from Schema import Schema


class Database:

    def __init__(self,uri: str, database: str, collection: str):
        url = uri
        self.client = MongoClient(url,server_api=ServerApi('1'))
        self.db = self.client[database]
        self.collection = self.db[collection]


    def create(self,schema: Schema, data: dict):
        _id = str(uuid4())

        if not '_id' in data: data['_id'] = _id

        data = DataObject(data,schema).getData()

        self.collection.insert_one(data)

    def get(self,query: dict):
        return self.collection.find(query)

    def printAll(self):
        for i in self.collection.find():
            print(i)


