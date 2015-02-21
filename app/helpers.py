import math
from app import db
from app.models import Post

class BoardHelper:
    posts_per_page = 5
    def __init__(self, board_name):
        self.board_id = board_name
        self.posts = Post.query.order_by(Post.date.desc()).filter(Post.board == board_name).all()
        self.num_pages = math.ceil(len((self.posts))/self.posts_per_page)
    
    def set_page(self, page):
        self.cur_page = page

    def get_page(self):
        page = self.cur_page
        start = (page +  1) * self.posts_per_page - self.posts_per_page
        end = self.posts_per_page * page + self.posts_per_page 
        return self.posts[start:end]
    
    def paginate(self):
        page_list = []
        for page in range(self.num_pages):
            page_list.append(page)
        return page_list
            
