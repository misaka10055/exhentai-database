from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'ehDatabase.sqlite'))
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Work(Base):
    __tablename__ = 'ehWorkList'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    language = Column(String)
    parody = Column(String)
    character = Column(String)
    female = Column(String)
    male = Column(String)
    group = Column(String)
    artist = Column(String)
    misc = Column(String)
    uploader = Column(String)
    pages = Column(String)
    uploadTime = Column(String)

    def __repr__(self):
        return "<User(name='%s')>" % self.name


class Parody(Base):
    __tablename__ = 'ehParodyList'

    id = Column(Integer, primary_key=True)
    workId = Column(Integer)
    parody = Column(String)

    def __repr__(self):
        return "<User(workID='%s')>" % self.workId


class Character(Base):
    __tablename__ = 'ehCharacterList'

    id = Column(Integer, primary_key=True)
    workId = Column(Integer)
    character = Column(String)

    def __repr__(self):
        return "<User(workID='%s')>" % self.workId


class Female(Base):
    __tablename__ = 'ehFemaleList'

    id = Column(Integer, primary_key=True)
    workId = Column(Integer)
    parody = Column(String)

    def __repr__(self):
        return "<User(workID='%s')>" % self.workId
