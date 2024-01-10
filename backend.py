from pymongo import MongoClient

class SupplierDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['vendor_management']
        self.collection = self.db['suppliers']

    def add_supplier(self, data):
        return self.collection.insert_one(data).inserted_id

    def get_suppliers(self):
        return list(self.collection.find({}, {'_id': 0}))

    def update_supplier(self, sup_id, data):
        return self.collection.update_one({'supid': sup_id}, {'$set': data})

    def delete_supplier(self, sup_id):
        return self.collection.delete_one({'supid': sup_id})

    def search_suppliers(self, search_by, search_txt):
        query = {search_by: {"$regex": search_txt, "$options": "i"}}
        return list(self.collection.find(query, {'_id': 0}))
