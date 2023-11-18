from  app.models import Category,Product,User
def get_category():
    return Category.query.all()
def get_produces(kw):
    produce= Product.query

    if kw:
        produce=produce.filter(Product.name.contains(kw))
    return produce.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)