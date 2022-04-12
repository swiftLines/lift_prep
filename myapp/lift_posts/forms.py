from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LiftPostForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    lift = TextAreaField('Lift', validators=[DataRequired()])
    sets = IntegerField('Sets')
    reps = IntegerField('Reps')
    submit = SubmitField('Post')