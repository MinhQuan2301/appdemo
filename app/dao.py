from app.models import Category, Product, User
from app import app
import hashlib


def get_category():
    return Category.query.all()


def get_produces(kw, cate_id, page = None):
    produce = Product.query

    if kw:
        produce = produce.filter(Product.name.contains(kw))

    if cate_id:
        produce = produce.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page-1)*page_size

        return produce.slice(start, start + page_size)
    return produce.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()
