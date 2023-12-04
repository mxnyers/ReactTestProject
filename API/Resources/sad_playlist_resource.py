import os
from flask_restful import Resource, reqparse
import pandas as pd
import ast
import json

class SadPlaylistResource(Resource):
    def get(self):
        print(os.getcwd())
        data = pd.read_csv(r"Data-Sources\Sad Rap Playlisters with Success - Sheet1.csv", sep=",")
        data = data.to_json(r"Data-Sources\sad-rap.json", indent=1, orient='records')  # convert dataframe to json
        data_file = open("Data-Sources\sad-rap.json", "r")
        data = json.loads(data_file.read())
        data_file.close()
        return data, 200  # return data and 200 OK

    