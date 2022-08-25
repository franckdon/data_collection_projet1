from sqlalchemy import create_engine

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
        data.to_sql('devises', engine, index=False)
        return 'Data save'