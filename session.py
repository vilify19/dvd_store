from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql

engine = create_engine("mysql+pymysql://root:PotuS!3210@localhost:3306/DVD_STORE")

Session = sessionmaker(engine)
session = Session()
