from wtforms import Form, TextField, TextAreaField, validators

class PostForm(Form):
	title = TextField('Title', [validators.Required(),
				validators.Length(min=3, max=80)])
	body = TextAreaField('Body', [validators.Required(),
				validators.Length(min=20, max=1024)])
