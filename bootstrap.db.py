from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def main():
    engine = create_engine("mysql+pymysql://root:PotuS!3210@localhost:3306/DVD_STORE")
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()
