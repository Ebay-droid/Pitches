from . import db
from datetime import datetime

class Pitch(db.Model):

    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.Integer)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch = db.Column(db.String)
    
    def save_pitch(self):
      db.session.add(self)
      db.session.commit()
      
    @classmethod
    def get_pitches(cls,category):
      pitches=Pitch.query.filter_by(category).all()
      return pitches
    




