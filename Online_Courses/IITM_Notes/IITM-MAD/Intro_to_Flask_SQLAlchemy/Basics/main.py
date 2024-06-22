from flask import Flask
from flask import render_template, request

# SQLAlchemy and SQLAlchemy ORM via Flask SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# creating the app
app = Flask(__name__)

# we configure our database by setting the URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database/testDB.sqlite3"

'''
For the common case of having one Flask application all you have to do is to create your Flask application, load the configuration of choice and then create the SQLAlchemy object by passing it the application. Once created, that object then contains all the functions and helpers from both 'sqlalchemy' and 'sqlalchemy.orm'. Furthermore it provides a class called 'Model' that is a 'declarative_base' which can be used to declare models. This essentially replaces the 'Base' as used in SQLAlchemy.
'''
# We can do the above by:
db = SQLAlchemy(app)

# Alternatively we could have also done:
'''
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
'''

# Everything else remains the same, here as in SQLAlchemy, i.e. instead of importing the 'Base' model from SQLAlchemy, we are going to import the 'Base' from Flask SQLAlchemy through 'db.Model'. That's the ONLY difference.


# Defining the Schema for various Tables in the database

class User(db.Model):
    '''
    --- Schema ---

    table user
            user_id int
            name str
            email str
    '''
    __tablename__ = "user"
    user_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), unique=True)


class Article(db.Model):
    '''
    --- Schema ---

    table article
            article_id int
            title str
            content str
    '''
    __tablename__ = "article"
    article_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    # we define a relationship here via the 'article_authors' table:
    authors = db.relationship("User", secondary="article_authors")


class ArticleAuthors(db.Model):
    '''
    --- Schema ---

    table article_authors
            user_id int
            article_id int
    '''
    __tablename__ = "article_authors"
    user_id = db.Column(db.Integer(), db.ForeignKey("user.user_id"),
                        primary_key=True, nullable=False)
    article_id = db.Column(db.Integer(), db.ForeignKey("article.article_id"),
                           primary_key=True, nullable=False)


# Setting up the routes

@app.route("/", methods=["GET", "POST"])
def home():
    articles_list = Article.query.all()
    authors_list = User.query.all()
    return render_template("home.html", articles=articles_list, authors=authors_list)


@app.route("/article_home/<article_title>", methods=["GET", "POST"])
def article_home(article_title):
    article_selected = Article.query.filter(
        Article.title == article_title).first()
    article_authors = article_selected.authors
    article_content = article_selected.content
    return render_template("article_home.html", article_title=article_title, article_authors=article_authors, article_content=article_content)


@app.route("/author_home/<author_name>", methods=["GET", "POST"])
def author_home(author_name):
    author_articles = Article.query.filter(
        Article.authors.any(name=author_name))
    return render_template("author_home.html", author_articles=author_articles, author_name=author_name)


# Running the webapp in local environment
if __name__ == '__main__':
    # Run the Flask app
    app.run(
        debug=True,
    )
