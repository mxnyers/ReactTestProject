from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from Resources.sad_playlist_resource import SadPlaylistResource
from Resources.users_resource import UsersResource
from Resources.locations_resource import LocationsResource

app = Flask(__name__)
api = Api(app)

#api.add_resource(UsersResource, '/users')
api.add_resource(SadPlaylistResource, '/sad-playlists')
api.add_resource(LocationsResource, '/locations')

@app.after_request

def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    app.run()