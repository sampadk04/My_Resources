from main import engine, Session, User

# We create an instance of our Session, to add the new users and commit the change to the database.
local_session = Session(bind=engine)


# This extracts all the entries in the table 'User' onto the users list
users = local_session.query(User).all()
'''
Instead of querying all, if we wanted the read to be limited to the first 3 examples, then:
users = local_session.query(User).all()[:3]
'''

# Here, 'users' is a list of 'User' objects
for user in users:
    print(user.name, user.email)


'''
% python read_user.py

2022-06-14 17:10:42,015 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-06-14 17:10:42,016 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, users.date_created AS users_date_created 
FROM users
2022-06-14 17:10:42,016 INFO sqlalchemy.engine.Engine [generated in 0.00006s] ()
Dean deanwin@supernatural.com
Sam samwin@supernatural.com
John johnwin@supernatural.com
Bruce wayne@batman.com

%
'''

'''
Querying one specific 'User' object: (filtering queries)
In this case, we will be querying the 'users' table in the 'data.db' database,
to find the 'first' user with User.name == 'Dean'
'''
user_dean = local_session.query(User).filter(User.name == "Dean").first()
print(user_dean)

'''
% python read_user.py

2022-06-14 17:23:33,712 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-06-14 17:23:33,713 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, users.date_created AS users_date_created 
FROM users 
WHERE users.name = ?
 LIMIT ? OFFSET ?
2022-06-14 17:23:33,713 INFO sqlalchemy.engine.Engine [generated in 0.00007s] ('Dean', 1, 0)
User:
 id= 1
 name= Dean
 email= deanwin@supernatural.com

%
'''
