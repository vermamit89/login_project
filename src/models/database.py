from sqlalchemy import create_engine

SQL_DB_URL='sqlite:///./user.db'
engine=create_engine(SQL_DB_URL,connect_args={'check_same_thread':False})