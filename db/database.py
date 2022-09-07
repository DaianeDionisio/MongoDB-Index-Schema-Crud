import pymongo

class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "localhost:27017"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            tlsAllowInvalidCertificates=True # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)


