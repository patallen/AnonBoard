from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask.ext.wtf import Form

class PostForm(Form):
	title = TextField('Title', [DataRequired(), Length(min=3, max=80)]) 
	body = TextAreaField('Body', [DataRequired(), Length(min=10, max=1024)])
