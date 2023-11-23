from app import db, app
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import enum


class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100),
                    default="https://cdn.viettelstore.vn/Images/Product/ProductImage/452166194.jpeg")
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100), default=True)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # import hashlib
        #
        # u1 = User( name = ' Admin ', username = "admin",
        #           password=str(hashlib.md5('56789'.encode('utf-8')).hexdigest()),
        #           user_role = UserRoleEnum.ADMIN)
        # db.session.add(u1)
        # db.session.commit()
        # c1 = Category(name=' Moblie ')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        # d1 = Product(name='iPhone 13', price=25000000,
        #              image="https://cdn.viettelstore.vn/Images/Product/ProductImage/452166194.jpeg", category_id=1)
        # d2 = Product(name='iPhone 14 pro max', price=40000000,
        #              image="https://cdn.viettelstore.vn/Images/Product/ProductImage/1896224739.jpeg", category_id=2)
        # d3 = Product(name='iPhone 15 pro max', price=50000000,
        #              image="https://cdn.viettelstore.vn/Images/Product/ProductImage/291703442.jpeg", category_id=3)
        # d4 = Product(name='Xiaomi mi 11 lite 5g', price=9000000,
        #              image="https://tingtingmobile.com/wp-content/uploads/2021/11/xiaomi-mi-11-lite-5g-3_13-2.webp",
        #              category_id=1)
        # d5 = Product(name='Xiaomi 10t pro 5g', price=7500000,
        #              image="https://cdn2.cellphones.com.vn/x/media/catalog/product/x/i/xiaomi-mi-10t-pro_2_.jpg",
        #              category_id=2)
        # db.session.add_all([d1, d2, d3, d4, d5])
        # db.session.commit()
