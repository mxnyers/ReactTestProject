# import os
# from flask import flask, jsonify, make_response
from flask_restful import Resource, reqparse
from Model.playlist_genres_model import PlaylistGenresModel as Model
from Model.playlist_genres_model import db
# import ast
# import json

class PlaylistGenresResource(Resource): 
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('genre', type=str, required=True)
      
    def get(self, playlistId):
        playlist = Model.query.get(playlistId)
        if playlist:
            return {'id': playlist.id, 'genre': playlist.genre}
        return {'message': 'Playlist not found'}
        
    def post(self):
        """Add/Update playlist genre information"""
        args = self.parser.parse_args()
        playlist = Model(genre=args['genre'])
        db.session.add(playlist)
        db.session.commit()
        return {'id': playlist.id, 'genre': playlist.genre}, 201
        
        
    # def get(self):
    #     print(os.getcwd())
    #     data = pd.read_csv(, sep=",")
    #     data = data.to_json(r"Data-Sources\sad-rap.json", indent=1, orient='records')  # convert dataframe to json
    #     data_file = open("Data-Sources\sad-rap.json", "r")
    #     data = json.loads(data_file.read())
    #     data_file.close()
    #     return data, 200  # return data and 200 OK

    # def post(self):