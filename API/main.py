from flask import Flask
from flask_restful import Api
from Resources.users_resource import UsersResource
from Resources.locations_resource import LocationsResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UsersResource, '/users')
api.add_resource(LocationsResource, '/locations')

if __name__ == "__main__":
    app.run()