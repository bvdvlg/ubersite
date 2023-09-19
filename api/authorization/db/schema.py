from sqlalchemy_utils import PasswordType, force_auto_coercion
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, VARCHAR, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker, relationship
from sqlalchemy.orm import validates
from sqlalchemy.schema import UniqueConstraint

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

    login = Column(VARCHAR(40), nullable=False, unique=True)
    email = Column(VARCHAR(40), nullable=False, unique=True)
    passwd = Column(PasswordType(max_length=1094,
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ), nullable=False)
    tokens = relationship("Tokens", backref="user")

    @validates("email", "login", "passwd")
    def not_empty(self, key, value):
        if value == "":
            return None
        return value

class Tokens(BaseModel):
    __tablename__ = 'tokens'
    __table_args__ = (
        UniqueConstraint('key', 'user_id', name='unique_key_check'),
    )

    token = Column(VARCHAR(40), nullable=False, unique=True)
    key = Column(VARCHAR(40), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    @validates("token", "key")
    def not_empty(self, key, value):
        if value == "":
            return None
        return value
