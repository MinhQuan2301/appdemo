from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "1234567890!@#$%^&*()qwertyuioplkjhgfdsazxcvbnm,./ASDFGHJKLZMXNCBVQWERTYUIOP"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saleapp?charset=utf8mb4" % quote("d@Ikaquan2301")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 3

db = SQLAlchemy(app=app)
login = LoginManager(app=app)

