

from Flask import Flask, request, current_app
from Flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_store.db'
db = SQLAlchemy(app)


#create the Book "table"
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.name} - {self.author} - {self.publisher}"

#I had problems with the app.app_context() but I think this is useless
#with app.app_context():
    # within this block, current_app points to app.
#    print (current_app.name)

#this will be like the homescreen
@app.route('/')
def index():
    return 'BOOOOKS!'

#This will show all the books
@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        print(book)
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher}
        print(book_data)
        output.append(book_data)

    return {"books": output}

#This one will basically get the id from the user and show the specific book information
@app.route('/books/<id>/')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.name, "author": book.author, "publisher": book.publisher}


#These wwere in the video so I just added them because why not
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'],
                  author=request.json['author'],
                    publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"404"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "The book has been removed"}