from app.models import *
from app import db

boards = {
	['b', 'random', 'dat dude done did it'],
	['x', 'paranormal', 'for all things weird'],
	['fit', 'fitness', 'get your swole on'],
	['r', 'requests', 'need something? request it.'],
}

for b in board:
	b = Board(b[0], b[1], b[2])
	db.session.add(b)

db.session.commit()
