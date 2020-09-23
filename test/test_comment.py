from app.models import Comment
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
  

    def setUp(self):
      self.comment=Comment(id =1,posted ='5/6/2005 09:34:42 PM',user_id=2,comment='there you go',pitch_id=5)
      
    def test_comment_instance_variables(self):  
      self.assertEquals(self.comment.id,1)
      self.assertEquals(self.comment.posted,'5/6/2005 09:34:42 PM')
      self.assertEquals(self.comment.user_id,2)
      self.assertEquals(self.comment.pitch_id,5)
      
   