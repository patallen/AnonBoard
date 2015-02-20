from flask import render_template, redirect, g
from app import app, db
from sqlalchemy.sql import exists
from app.models import *
from app.forms import PostForm
import datetime

@app.context_processor
def header_helper():
    return dict(boards=Board.query.all())


@app.route('/')
def homepage():
    return render_template('index.html') 


@app.route('/<board>', methods=['GET', 'POST'])
def boardpage(board):
    postform = PostForm()
    if postform.validate_on_submit():
        p = Post(board, postform.title.data, postform.body.data, datetime.datetime.utcnow())
        db.session.add(p)
        db.session.commit()
        postform.reset()
    # Redirect to home page if board does not exist
    if Board.query.filter(Board.name == board).all()== [] :
        return redirect('/')

    posts = Post.query.filter(Board.name == board).all()
    return render_template('board.html', posts=posts, form=postform)



