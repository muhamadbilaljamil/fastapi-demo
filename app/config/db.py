# from sqlalchemy import create_engine, MetaData

# # dialect+driver://username:password@host:port/database
# engine = create_engine('mysql+pymysql://root:root@localhost:3306/python_demo')

# meta = MetaData()
# conn = engine.connect()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:root@localhost:3306/python_demo'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
