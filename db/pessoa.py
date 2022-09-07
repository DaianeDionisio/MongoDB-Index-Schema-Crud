from db.database import Database
from bson.objectid import ObjectId

class PessoaDAO:
    def __init__(self):
        self.db = Database(database="livros",collection="Livros")
        self.collection = self.db.collection

    def read_all(self):
        res = self.collection.find()
        return res

    def update_price(self, id: str,preco: float):
        res = self.collection.update_one({"_id": ObjectId(id)},{"$set": {"preco": preco}})
        return res.modified_count

    def create_book(self, titulo: str, autor: str, ano: int, preco: float):
        res = self.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
        return res.inserted_id

    def delete_book(self, id: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count

