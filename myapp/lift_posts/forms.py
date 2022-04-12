from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LiftPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    lift = TextAreaField('Lift', validators=[DataRequired()])
    submit = SubmitField('Post')