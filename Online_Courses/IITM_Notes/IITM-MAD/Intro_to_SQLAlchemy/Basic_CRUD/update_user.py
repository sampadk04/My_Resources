from main import engine, Session, User

# We create an instance of our Session, to add the new users and commit the change to the database.
local_session = Session(bind=engine)

'''
Suppose we want to change the email id of the user, who has name='John'
'''
# select the user
user_to_update = local_session.query(User).filter(User.name == "John").first()
# update the fields
user_to_update.email = "stewart@lantern.com"

# commit the changes onto the database
local_session.commit()

'''
% python update_user.py

2022-06-14 17:34:27,612 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-06-14 17:34:27,613 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, users.date_created AS users_date_created 
FROM users 
WHERE users.name = ?
 LIMIT ? OFFSET ?
2022-06-14 17:34:27,613 INFO sqlalchemy.engine.Engine [generated in 0.00007s] ('John', 1, 0)
2022-06-14 17:34:27,616 INFO sqlalchemy.engine.Engine UPDATE users SET email=? WHERE users.id = ?
2022-06-14 17:34:27,616 INFO sqlalchemy.engine.Engine [generated in 0.00009s] ('stewart@lantern.com', 3)
2022-06-14 17:34:27,616 INFO sqlalchemy.engine.Engine COMMIT

%
'''
