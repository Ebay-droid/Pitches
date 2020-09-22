
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile,CommentForm
import markdown2
from flask_login import login_required,current_user
from  ..models import Pitch,User,Comment,Like
from .. import db,photos


@main.route('/')
def index():
  
  return render_template('index.html')


@main.route('/pitches/new_pitch',methods = ['GET','POST'])
@login_required
def new_pitch():
  form = PitchForm()
#   pitches = Pitch.query.filter_by(user_id).all()
  
  if form.validate_on_submit():
    category =form.category.data
    pitch =form.pitch.data
    # user_id= user_id
    
    #pitch instance
    new_pitch =  Pitch(pitch=pitch,user =current_user,category=category)
    
    #save_pitch
    new_pitch.save_pitch()
    return redirect(url_for('.new_pitch'))

    
  return render_template('new_pitch.html', pitch_form=form )  

@main.route('/pitches/comment/<int:pitch_id>',methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    # pitches = Pitch.query.get(pitch_id)
    
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        new_comment = Comment(comment = comment, pitch_id=pitch_id)
        
        
        new_comment.save_comment()
        return redirect(url_for('.index',form =form,pitch_id =pitch_id))
    
    return render_template('comments.html', comment_form =form, comments = comments, pitch_id =pitch_id)


# @main.route('/user/my_pitches')
# def my_pitches(user_id):
#     user = User.query.filter_by(username = 'uname').first()
#     pitches = Pitch.query.filter_by(user_id).all()
#     user = current_user
    
#     return render_template ('profile.html',pitches = pitches, user = user)


@main.route('/pitches')
def get_pitches():
    user = User.query.filter_by(username = 'uname').first()
    pitches = Pitch.query.all()
    user = current_user
    
    return render_template ('pitch.html',pitches = pitches, user = user)




  
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


@main.route('/counter')
@login_required
def Upvote():
    like = 0
    like += 1