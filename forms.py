from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class DataForm(FlaskForm):
    Title = StringField('MovieTitle')
    Director = StringField('Director')
    Rank = StringField('Rank')
    Rating = StringField('Rating')
    Year = StringField('Year')
    Submit = SubmitField('Submit')