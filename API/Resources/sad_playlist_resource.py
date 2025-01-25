import os
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
import pandas as pd
import ast
import json

class SadPlaylistResource(Resource):
    def __init__(self):
        self.data_file = r"API\Data-Sources\Genre-Specific-Playlists\SadRap.csv"
        self.data = pd.read_csv(self.data_file, sep=",")
        self.data.fillna("", inplace=True)
        
    def save_data(self):
        # Save json data back to our data source.
        self.data.to_csv(self.data_file, index=False)       
      
    def get(self, playlistId=None):
        if playlistId == None:
            # Return all playlists
            new_data = jsonify(self.data.to_dict(orient="records"))
            return make_response(jsonify(self.data.to_dict(orient="records")), 200)
        
        else:
            playlist = self.data[self.data['id']] == playlistId
            if playlist.empty:
                return {'error': 'Playlist not found'}, 404
            return make_response(jsonify(playlist.to_dict(orient="records")[0]), 200)
        
    def post(self):
        """Add a new playlist"""
        
    # def get(self):
    #     print(os.getcwd())
    #     data = pd.read_csv(, sep=",")
    #     data = data.to_json(r"Data-Sources\sad-rap.json", indent=1, orient='records')  # convert dataframe to json
    #     data_file = open("Data-Sources\sad-rap.json", "r")
    #     data = json.loads(data_file.read())
    #     data_file.close()
    #     return data, 200  # return data and 200 OK

    # def post(self):