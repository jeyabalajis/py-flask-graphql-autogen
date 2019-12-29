from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def __get_db_engine():
    """
    protected method. Implement additional methods as required to create database string
    """
    engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
    return engine


def get_db_session():
    """

    """
    engine = __get_db_engine()
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    return db_session
