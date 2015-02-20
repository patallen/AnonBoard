from flask import render_template, redirect
from app import app, db
from sqlalchemy.sql import exists
from app.models import *
from app.forms import PostForm

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<board>', methods=['GET', 'POST'])
def boardpage(board):
    postform = PostForm()
    # Redirect to home page if board does not exist
    if Board.query.filter(Board.name == board).all()== [] :
        return redirect('/')
    if postform.validate_on_submit():
        print(postform.title)
    posts = Post.query.filter(Board.name == board).all()
    print(posts) 
    return render_template('board2.html', posts=posts, form=postform)
