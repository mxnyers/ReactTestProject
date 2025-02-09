from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource

class DynamicResource(Resource):
    def __init__(self, model, db):
        self.model = model
        self.db = db
        

    def get(self, item_id=None):
        if item_id:
            item = self.model.query.get(item_id)
            if item:
                return jsonify({col.name: getattr(item, col.name) for col in item.__table__.columns})
            return {'message': 'Item not found'}, 404
        items = self.model.query.all()
        return jsonify([{col.name: getattr(i, col.name) for col in i.__table__.columns} for i in items])

    def post(self):
        data = request.get_json()
        new_item = self.model(**data)
        self.db.session.add(new_item)
        self.db.session.commit()
        return {'message': 'Item added successfully'}, 201

    def put(self, item_id):
        data = request.get_json()
        item = self.model.query.get(item_id)
        if not item:
            return {'message': 'Item not found'}, 404
        for key, value in data.items():
            setattr(item, key, value)
        self.db.session.commit()
        return {'message': 'Item updated successfully'}

    def delete(self, item_id):
        item = self.model.query.get(item_id)
        if not item:
            return {'message': 'Item not found'}, 404
        self.db.session.delete(item)
        self.db.session.commit()
        return {'message': 'Item deleted successfully'}