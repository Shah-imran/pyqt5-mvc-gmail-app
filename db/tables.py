from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text, JSON
from sqlalchemy.ext.declarative import declarative_base
from config import AppConfig

db_path = f"{AppConfig.base_dir}/group.db"

Base = declarative_base()
engine = create_engine(
    f'sqlite:///{db_path}', connect_args={'check_same_thread': False}, echo=False)


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    first_from_name = Column(String)
    last_from_name = Column(String)
    email = Column(String)
    email_pass = Column(String)
    proxy_port = Column(String)
    proxy_user = Column(String)
    proxy_pass = Column(String)
    group_name = Column(String)


class Target(Base):
    __tablename__ = 'target'

    id = Column(Integer, primary_key=True)
    one = Column(String)
    two = Column(String)
    three = Column(String)
    four = Column(String)
    five = Column(String)
    six = Column(String)
    to_name = Column(String)
    email = Column(String)

# todo : create inbox class


Base.metadata.create_all(engine)