from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import select

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    '''
    --- Schema ---

    table user
            user_id int
            name str
            email str
    '''
    __tablename__ = "user"
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(), unique=True)
    email = Column(String(), unique=True)
    # we can also define a relationship here via the 'article_authors' table:
    # articles = relationship("Article", secondary="article_authors")


class Article(Base):
    '''
    --- Schema ---

    table article
            article_id int
            title str
            content str
    '''
    __tablename__ = "article"
    article_id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String())
    content = Column(String())
    # we define a relationship here via the 'article_authors' table:
    authors = relationship("User", secondary="article_authors")

# This table will store the information regarding the authors that wrote an article. This will be a many to many relationship as multiple authors can be involved in a single article and a singlr author might have written multiple articles.


class ArticleAuthors(Base):
    '''
    --- Schema ---

    table article_authors
            user_id int
            article_id int
    '''
    __tablename__ = "article_authors"
    user_id = Column(Integer(), ForeignKey("user.user_id"),
                     primary_key=True, nullable=False)
    article_id = Column(Integer(), ForeignKey("article.article_id"),
                        primary_key=True, nullable=False)

# Now, we define a 'Many To Many' relationship between 'user' and 'article'.
# Documentation link: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html


# This helps connect to a database and helps us communicate with the database
# We will be using a pre-filled database, as created in thescreen-cast tutorial in MAD-1, week-5. We place the 'testDB.sqlite3' file in the 'database' folder. This was created and viewed using the 'DB Browser for SQLite' tool.
engine = create_engine("sqlite:///database/testDB.sqlite3", echo=False)

# Now, we can get a connection and run queries.
# This is an example of that:

'''
if __name__ == '__main__':
    # we create a statement 'stmt' to select the 'user' table in the database
    stmt = select(User)
    print("---------QUERY---------")
    print(stmt)

    # we create a connection named 'conn'
    with engine.connect() as conn:
        print("---------RESULT---------")
        for row in conn.execute(stmt):
            print(row)
'''

'''
% python main.py

---------QUERY---------
SELECT "user".user_id, "user".name, "user".email 
FROM "user"
---------RESULT---------
(1, 'Sam', 'samwin@gmail.com')
(2, 'Dean', 'deanwin@gmail.com')
(3, 'Charlie', 'charlie@gmail.com')

%
'''

# Usually, we don't try to get a connection every time, we use something called a 'Session'. The 'Session' establishes all conversations with the database and represents a “holding zone” for all the objects loaded or associated with it during its lifespan.
# Documentation Link: https://docs.sqlalchemy.org/en/14/orm/session_basics.html

'''
if __name__ == '__main__':
    # create a session and read the objects. We can similarly, create, update, delete as well.
    with Session(bind=engine) as session:
        # Here, we query to find all the articles in the 'Article' table, which have 'article_id == 1'
        articles = session.query(Article).filter(Article.article_id == 1).all()
        for article in articles:
            print("Article Title:", article.title)
            # We extract the authors of this article, from the relationship as defined in the 'Article' class.
            print("Article Authors:")
            for author in article.authors:
                print(author.name)
'''

'''
% python main.py

Article Title: Cricket
Article Authors:
Charlie

%
'''


# We can also create transactions using session. Transactions are 'atomic' in nature. The process either finishes completely, and if it is interrupted in the middle, it reverts back to the original state before the process began.

'''
if __name__ == '__main__':
    with Session(bind=engine, autoflush=False) as session:
        session.begin()
        # error handling of transaction with try, except, else blocks
        try:
            # we create a new 'Article' object which we want to add
            article_1 = Article(
                title="Hockey", content="Hockey is India's national game. India has won many olympic gold medals in hockey during the pre and post independence era. Currently Indian Hockey is being sponsored by the Govt. of Odisha.")
            # add this new 'Article' object to the 'article' table
            session.add(article_1)
            session.flush()
            # This sends the article to the database

            # This is the auto-incremented id of this article, created after adding it to the database
            print("--------Get article_id-------")
            print(article_1.article_id)

            # Suppose article_1, has 2 authors with user_id = 1 and user_id = 2. We update this using the 'article_authors' table by adding 'ArticleAuthors' objects to this table.
            article_1_author_1 = ArticleAuthors(
                user_id=1, article_id=article_1.article_id)
            article_1_author_2 = ArticleAuthors(
                user_id=2, article_id=article_1.article_id)
            # add these new 'ArticleAuthors' objects to the 'article_authors' table
            session.add(article_1_author_1)
            session.add(article_1_author_2)
        except:
            # If any error happens, the entire operation rolls back to the original state. This makes this operation a 'transaction' (atomic), and this is handles in the 'except' block.
            print("Rolling Back...")
            session.rollback()
            raise
        else:
            # If everything goes well, we commit the changes to the database.
            print("Commit...")
            session.commit()
'''

'''
# Example: When the changes commit without any errors and rollbacks. The new article, with title 'Hockey' also gets added to the database.
% python main.py

--------Get article_id-------
3
Commit...

%
'''

'''
if __name__ == '__main__':
    with Session(bind=engine, autoflush=False) as session:
        session.begin()
        # error handling of transaction with try, except, else blocks
        try:
            # we create a new 'Article' object which we want to add
            article_1 = Article(
                title="Kabaddi", content="Kabaddi is one of the more indegenious games in India. The Pro Kabaddi League as aired in Star Sports shot the sports into popularity throughout India.")
            # add this new 'Article' object to the 'article' table
            session.add(article_1)
            session.flush()
            # This sends the article to the database

            # This is the auto-incremented id of this article, created after adding it to the database
            print("--------Get article_id-------")
            print(article_1.article_id)

            # We raise an artificial error here, to make shift the code to the 'except' block to check the 'rollback' effect. Even the the database added the new article into the database after the flushing, the rollback makes sure that it is removed.
            raise Exception("Dummy Error!")

            # Suppose article_1, has 2 authors with user_id = 1 and user_id = 2. We update this using the 'article_authors' table by adding 'ArticleAuthors' objects to this table.
            article_1_author_1 = ArticleAuthors(
                user_id=3, article_id=article_1.article_id)
            # add these new 'ArticleAuthors' objects to the 'article_authors' table
            session.add(article_1_author_1)
        except:
            # If any error happens, the entire operation rolls back to the original state. This makes this operation a 'transaction' (atomic), and this is handles in the 'except' block.
            print("Rolling Back...")
            session.rollback()
            raise
        else:
            # If everything goes well, we commit the changes to the database.
            print("Commit...")
            session.commit()
'''

'''
# Example: When the changes don't commit and the steps are rolled back due to some error.
% python main.py

--------Get article_id-------
4
Rolling Back...
Traceback (most recent call last):
  File "/Users/sampadk04/Desktop/Programming/VSCode-Projects/MAD/Intro_to_SQLAlchemy/Advanced_SQLAlchemy/main.py", line 197, in <module>
    raise Exception("Dummy Error!")
Exception: Dummy Error!

%
'''

# Instead of adding the relationship between the new 'article' and it's authors using the 'article_author' table and 'ArticleAuthors' object, we can directly specify the relationships via 'article.authors' relationship in the class 'Article'.

if __name__ == '__main__':
    with Session(bind=engine, autoflush=False) as session:
        session.begin()
        # error handling of transaction with try, except, else blocks
        try:
            # we create a new 'Article' object which we want to add
            article_1 = Article(
                title="Using Relationship", content="Instead of adding the relationship between the new 'article' and it's authors using the 'article_author' table and 'ArticleAuthors' object, we can directly specify the relationships via 'article.authors' relationship in the class 'Article'.")

            # We extract the 'User' objects which we want to add as the authors for 'article_1' using the relationship. We do this by query and filter.
            author_1 = session.query(User).filter(User.name == "Sam").first()
            author_2 = session.query(User).filter(
                User.name == "Charlie").first()

            # Now, we add these authors corresponding to 'article_1', via the relationship, article_1.authors
            article_1.authors.append(author_1)
            article_1.authors.append(author_2)

            # add this new 'Article' object to the 'article' table
            session.add(article_1)
            # This sends the article to the database
        except:
            # If any error happens, the entire operation rolls back to the original state. This makes this operation a 'transaction' (atomic), and this is handles in the 'except' block.
            print("Rolling Back...")
            session.rollback()
            raise
        else:
            # If everything goes well, we commit the changes to the database.
            print("Commit...")
            session.commit()


'''
% python main.py

Commit...

%
'''
