from main import engine, Session, User

# We create an instance of our Session, to add the new users and commit the change to the database.
local_session = Session(bind=engine)

'''
Suppose we want to delete the user with name='Sam'
'''
# select the user
user_to_delete = local_session.query(User).filter(User.name == "Sam").first()
# delete the selected_user
local_session.delete(user_to_delete)

# commit the changes onto the database
local_session.commit()

'''
% python delete_user.py

2022-06-14 17:43:40,677 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-06-14 17:43:40,678 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, users.date_created AS users_date_created 
FROM users 
WHERE users.name = ?
 LIMIT ? OFFSET ?
2022-06-14 17:43:40,678 INFO sqlalchemy.engine.Engine [generated in 0.00007s] ('Sam', 1, 0)
2022-06-14 17:43:40,680 INFO sqlalchemy.engine.Engine DELETE FROM users WHERE users.id = ?
2022-06-14 17:43:40,680 INFO sqlalchemy.engine.Engine [generated in 0.00005s] (2,)
2022-06-14 17:43:40,680 INFO sqlalchemy.engine.Engine COMMIT

%
'''
