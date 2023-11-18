from flask import render_template, request
import dao
from app import app,login


@app.route('/')
def index():
    kw=request.args.get("kw")
    pro=dao.get_produces(kw)
    cas=dao.get_category()
    return render_template('index.html', categories=cas, produces=pro)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)
if __name__=='__main__':
    from  app import admin
    app.run(debug=True)
