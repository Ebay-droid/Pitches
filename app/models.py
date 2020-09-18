from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

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
    
class User(db.Model):  
      __tablename__ = 'users'

      id = db.Column(db.Integer,primary_key = True)
      username = db.Column(db.String(255))
      role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
      pass_secure = db.Column(db.String(255))
      
      
      @property
      def password(self):
          raise AttributeError('You cannot read the password attribute')

      @password.setter
      def password(self, password):
          self.pass_secure = generate_password_hash(password)


      def verify_password(self,password):
          return check_password_hash(self.pass_secure,password)

      def __repr__(self):
          return f'User {self.username}'
        
        
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'      
    




