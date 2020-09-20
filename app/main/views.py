
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile
import markdown2
from flask_login import login_required,current_user
from  ..models import Pitch,User
from .. import db,photos


@main.route('/')
def index():
  
  return render_template('index.html')


@main.route('/pitches/new_pitch',methods = ['GET','POST'])
@login_required
def new_pitch():
  form = PitchForm()
  
  if form.validate_on_submit():
    title =form.title.data
    pitch =form.pitch.data
    
    #pitch instance
    new_pitch =  Pitch(pitch=pitch,user =current_user)
    
    #save_pitch
    new_pitch.save_pitch()
    return redirect(url_for('.pitch'))

  return render_template('new_pitch.html', pitch_form=form)  
    
    
# @main.route('/pitch/<category>')
# def single_pitch(category):
#     pitch=Pitch.query.get(category)
#     if pitch is None:
#         abort(404)
#     format_pitch = markdown2.markdown(pitch.pitch,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('pitch.html',pitch = pitch,format_pitch=format_pitch) 
  
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)     
    
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))