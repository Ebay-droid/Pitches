from app.models import Pitch
from app import db
import unittest

  

def setUp(self):
        self.pitch= Pitch(1,'Marketing','5/6/2005 09:34:42 PM',1,'heey','yaay')
    
def test_check_instance(self):
    self.assertEquals(self.pitch.id, 1)
    self.assertEquals(self.pitch.category,'Marketing')
    self.assertEquals(self.pitch.posted,'5/6/2005 09:34:42 PM')      
    self.assertEquals(self.pitch.user_id,1)  
    self.assertEquals(self.pitch.pitch,'heey')
    self.assertEquals(self.pitch.comment,'yaay')
    
    
def test_save_pitch(self):  
  self.pitch.save_pitch()
  self.assertTrue(len(Pitch.query.all())>0)    
          
