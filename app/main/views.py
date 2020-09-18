
from flask import render_template
from . import main
from .forms import PitchForm
import markdown2

@main.route('/pitches/category',methods = ['GET','POST'])
def new_pitch(category):
  form = PitchForm()
  
  if form.validate_on_submit():
    title =form.title.data
    pitch =form.review.data
    
    #pitch instance
    new_pitch =  Pitch(category= category,pitch=pitch,)
    
    #save_pitch
    new_pitch.save_pitch()
    
    
    
