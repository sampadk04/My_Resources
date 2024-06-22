from main import Base, engine, User

Base.metadata.create_all(engine)
# When we run this file in terminal, this will create the database 'data.db' in the '/database/data.db',
# which we can explore in DB Browser for sqlite.
