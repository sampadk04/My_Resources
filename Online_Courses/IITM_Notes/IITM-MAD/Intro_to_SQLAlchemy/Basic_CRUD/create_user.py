from main import engine, Session, User

# We create an instance of our Session, to add the new users and commit the change to the database.
local_session = Session(bind=engine)

# Create User instances to be added.
# These objects in-built constructors by default.

user_1 = User(id=1, name="Dean", email="deanwin@supernatural.com")
user_2 = User(id=2, name="Sam", email="samwin@supernatural.com")
user_3 = User(id=3, name="John", email="johnwin@supernatural.com")
user_4 = User(id=4, name="Bruce", email="wayne@batman.com")

# adding the datas to the 'users' table
local_session.add(user_1)
local_session.add(user_2)
local_session.add(user_3)
local_session.add(user_4)

# commit the changes onto the database
local_session.commit()

# When we run this file in terminal, it will add all these 'User' instances into the 'users' table in 'data.db' database.

'''
% python create_user.py

2022-06-14 16:58:11,789 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-06-14 16:58:11,790 INFO sqlalchemy.engine.Engine INSERT INTO users (id, name, email, date_created) VALUES (?, ?, ?, ?)
2022-06-14 16:58:11,790 INFO sqlalchemy.engine.Engine [generated in 0.00011s] ((1, 'Dean', 'deanwin@supernatural.com', '2022-06-14 11:28:11.790510'), (2, 'Sam', 'samwin@supernatural.com', '2022-06-14 11:28:11.790515'), (3, 'John', 'johnwin@supernatural.com', '2022-06-14 11:28:11.790516'), (4, 'Bruce', 'wayne@batman.com', '2022-06-14 11:28:11.790517'))
2022-06-14 16:58:11,792 INFO sqlalchemy.engine.Engine COMMIT

%
'''
