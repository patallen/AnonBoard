from app import db

class Board(db.Model):
    __tablename__ = 'boards'

    name = db.Column(db.String(20), primary_key=True)
    brief = db.Column(db.String(20), unique=True)
    desc = db.Column(db.String(140))
    # posts = db.relationship('Post', backref='board', lazy='dynamic')

    def __init__(self, name, brief, desc):
        self.name = name
        self.brief = brief
        self.desc = desc
        
    def __repr__(self):
        return '<Name %r>' % self.name


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    board = db.Column(db.String(20), db.ForeignKey('boards.name'))
    title = db.Column(db.String(64))
    body = db.Column(db.String(1024))
    date = db.Column(db.DateTime())
    
    def __init__(self, board, title, body, date):
        self.board = board 
        self.title = title 
        self.body = body
        self.date = date
     

    def __repr__(self):
        return '<ID %r>' % self.id

