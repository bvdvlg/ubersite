from sqlalchemy_utils import PasswordType, force_auto_coercion
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, VARCHAR, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker, relationship

'''engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432")

force_auto_coercion()

Session = sessionmaker()
session = Session(bind=engine)'''

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)

class Users(BaseModel):
    __tablename__ = 'users'

    login = Column(VARCHAR(40), nullable=False)
    email = Column(VARCHAR(40), nullable=False)
    tokens = relationship("Tokens", backref="user")

class UsersPrivate(BaseModel):
    __tablename__ = 'passwords'

    passwd = Column(PasswordType(max_length=1094,
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))

class Tokens(BaseModel):
    __tablename__ = 'tokens'

    token = Column(VARCHAR(40), nullable=False)
    key = Column(VARCHAR(40), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
