from flask import render_template, redirect, g
from app import app, db
from sqlalchemy.sql import exists
from app.models import *
from app.forms import PostForm
from app.helpers import BoardHelper
import datetime

@app.context_processor
def header_helper():
    return dict(boards=Board.query.all())


@app.route('/')
def homepage():
    return render_template('index.html') 


@app.route('/<board_id>', methods=['GET', 'POST'])
@app.route('/<board_id>/<page_num>', methods=['GET', 'POST'])
def boardpage(board_id, page_num='0'):
    postform = PostForm()
    if postform.validate_on_submit():
        p = Post(board_id, postform.title.data, postform.body.data, datetime.datetime.utcnow())
        db.session.add(p)
        db.session.commit()
        return redirect ('/%s'% board_id)
    # Redirect to home page if board does not exist
    if Board.query.filter(Board.name == board_id).all()== [] :
        return redirect('/')

    board = BoardHelper(board_id)
    board.set_page(int(page_num))
    return render_template('board.html', board=board, form=postform)



