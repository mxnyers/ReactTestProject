from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()
    
class PlaylistGenresModel(db.Model):
    """Model class that emulates the database table: playlist_genres"""
    __tablename__ = "playlist_genres"
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<PlatlistGenreModel {self.genre}>'
    
    # def __init__(self, database, dbModel):
    #         self.id =  