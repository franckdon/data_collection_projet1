from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Credentials to database connection
hostname="127.0.0.1:8889"
dbname="dataCollection"
uname="root"
pwd="root"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

class dataSave(object):

    @classmethod
    def getData(cls, data):
        data.to_sql('devises', engine, index=True)
        return 'Data save'

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()