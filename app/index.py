from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user




@app.route('/')
def index():
    kw = request.args.get("kw")
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')
    pro = dao.get_produces(kw, cate_id, page)
    cas = dao.get_category()
    return render_template('index.html', categories=cas, produces=pro)


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user)
        return redirect('/admin')


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__=='__main__':
    from  app import admin
    app.run(debug=True)
