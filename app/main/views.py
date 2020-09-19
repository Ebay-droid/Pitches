
from flask import render_template
from . import main
from .forms import PitchForm
import markdown2
from flask_login import login_required
from app.models import Pitch


@main.route('/pitch/new/category',methods = ['GET','POST'])
@login_required
def new_pitch(category):
  form = PitchForm()
  
  if form.validate_on_submit():
    title =form.title.data
    pitch =form.review.data
    
    #pitch instance
    new_pitch =  Pitch(category= category,pitch=pitch,)
    
    #save_pitch
    new_pitch.save_pitch()
    
    
@main.route('/pitch/category')
def single_pitch(id):
    pitch=Pitch.query.get(id)
    if pitch is None:
        abort(404)
    format_pitch = markdown2.markdown(pitch.pitch,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('pitch.html',pitch = pitch,format_pitch=format_pitch)    
    
    
    
