from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask.ext.wtf import Form
from werkzeug.datastructures import MultiDict

class PostForm(Form):
    title = TextField('Title', [DataRequired(), Length(min=3, max=80)]) 
    body = TextAreaField('Body', [DataRequired(), Length(min=10, max=1024)])

    def reset(self):
        blank_data = MultiDict([])
        self.process(blank_data)
