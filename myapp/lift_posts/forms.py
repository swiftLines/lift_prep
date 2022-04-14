from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# class ProgramForm(FlaskForm):
#     lift = (TextAreaField('Lift', validators=[DataRequired()]))
#     sets = IntegerField('Sets')
#     reps = IntegerField('Reps')

class LiftPostForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    # lifts = FieldList(FormField(ProgramForm), max_entries=10)
    lift = TextAreaField('Lift', validators=[DataRequired()])
    sets = IntegerField('Sets')
    reps = IntegerField('Reps')
    submit = SubmitField('Post')