from pymongo import MongoClient

address='localhost'
port=27017
db='learn'
coll='inventory'

class ConnectionMongo:
    def __init__(self):

        print('connecting...')
        client = MongoClient()
        client = MongoClient(address, port)

        self.db = client[db]
        self.collections={}

    def returnCollection(self,coll_name=coll):

        self.collections[coll_name] = self.db[coll_name]
        return self.collections[coll_name]



