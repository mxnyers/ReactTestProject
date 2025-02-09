from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from Utility.model_generator import ModelGenerator
from Resources.dynamic_resource import DynamicResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://DESKTOP-LOBD6GT\\SQLEXPRESS/PlaylistPitcher?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
db = SQLAlchemy(app)
api = Api(app)

# Generate models for all tables
with app.app_context():
    generated_models = ModelGenerator(db=db).models

# Dictionary to store dynamically created resource classes
dynamic_resources = {}

# Function to dynamically create and add resources for each model
def add_resource_for_model(model, endpoint_name):
    resource_class = type(f"{endpoint_name}Resource", (DynamicResource,), {
        '__init__': lambda self: DynamicResource.__init__(self, model, db=db)
    })
    dynamic_resources[endpoint_name] = resource_class
    api.add_resource(resource_class, f'/{endpoint_name}', f'/{endpoint_name}/<int:item_id>')

# Adding resources dynamically for all tables
for table_name, model in generated_models.items():
    add_resource_for_model(model, table_name)

@app.after_request

def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    app.run()