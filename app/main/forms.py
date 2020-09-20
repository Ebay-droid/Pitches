from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = SelectField('Category', choices = [('Job','Job'),('Interview','Interview'),('Band','Band'),('Business','Business')], validators = [Required()]),
    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch', )
    submit = SubmitField('Submit')
    
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')      