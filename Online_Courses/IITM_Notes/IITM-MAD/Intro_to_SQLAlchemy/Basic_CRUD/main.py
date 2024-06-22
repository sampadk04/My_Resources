# using declarative_base, we create our base class from which we inherit and create our schema table.
from sqlalchemy.orm import declarative_base
# for CRUD operations
from sqlalchemy.orm import sessionmaker
# these are used to create the schema in the table object
from sqlalchemy import Column, String, Integer, DateTime
# to create database and database tables
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

engine = create_engine("sqlite:///database/data.db", echo=True)

Session = sessionmaker()


class User(Base):  # This creating a schema
    '''
    --- Schema ---

    table users
        id int
        name str
        email str
        date_created datetime
    '''
    __tablename__ = "users"  # This is going to be the 'name' of the table in the database
    id = Column(Integer(), primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    # to print instances of this class
    def __repr__(self) -> str:
        return f"User:\n id= {self.id}\n name= {self.name}\n email= {self.email}\n"


'''
# creating a new instance of this object. These objects in-built constructors by default.
# If we add the following lines of code to our file
new_user_1 = User(id=1, name="Dean", email="deanwin@supernatural.com")
print(new_user_1)

This prints the following in terminal:
User:
 id= 1
 name= Dean
 email= deanwin@supernatural.com
'''

'''
In the python interpreter we can carry out the following tasks:
>>> from main import User
>>> User
<class 'main.User'>
>>> User.__tablename__
'users'
>>> User.__table__
Table('users', MetaData(), Column('id', Integer(), table=<users>, primary_key=True, nullable=False), Column('name', String(length=30), table=<users>, nullable=False), Column('email', String(length=80), table=<users>, nullable=False), Column('date_created', DateTime(), table=<users>, default=ColumnDefault(<function datetime.utcnow at 0x102a83160>)), schema=None)
>>> # This shows the metadata about this table and schema
'''

'''
To create database named 'data.db', run the 'create_db.py' file.
'''

'''
To use various CRUD operations, we need to use 'Session' instances.

First, create the 'data.db' file using 'create_db.py'.
Follow this order to make sense of the .py files:
- create_user.py
- read_user.py
- update_user.py
- delete_user.py
'''
