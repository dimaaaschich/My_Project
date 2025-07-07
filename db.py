from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker


engine = create_engine('postgresql://my_project_1:1234@localhost/my_project_1')

db_session = scoped_session(sessionmaker(bind=engine))

class Base(DeclarativeBase):
    pass