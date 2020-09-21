from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch(db.Model):

    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String, index = True)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch = db.Column(db.String)
    comments = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")
   
    
    def save_pitch(self):
      db.session.add(self)
      db.session.commit()
      
      
      
      
    def __repr__(self):
        return f'Pitch {self.post}'  
      
   
    
class User(UserMixin,db.Model):  
      __tablename__ = 'users'
      
      pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
      comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")  
      id = db.Column(db.Integer,primary_key = True)
      username = db.Column(db.String(255))
      email = db.Column(db.String(255),unique = True,index = True)
      bio = db.Column(db.String(255))
      profile_pic_path = db.Column(db.String())
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
        
        
     
    
  
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer,primary_key = True)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.Column(db.String)     
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    


    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments   
    
    def __repr__(self):
        return f'comment:{self.comment}' 
    
    
class Like(db.Model):
    __tablename__ = 'likes'
    
    id =db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id")) 
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))  

    def save_like(self):
        db.session.add(self)
        db.session.commit()
        
    def __repr__(self):
        return f'comment:{self.comment}'     



