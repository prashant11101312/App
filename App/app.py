from flask import Flask, render_template, request, redirect, url_for
from library_management_system import Library

app = Flask(__name__)

library = Library()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    isbn = request.form["isbn"]
    year = request.form["year"]
    library.add_book(title, author, isbn, year)
    return redirect(url_for("index"))

@app.route("/remove_book", methods=["POST"])
def remove_book():
    isbn = request.form["isbn"]
    library.remove_book(isbn)
    return redirect(url_for("index"))

@app.route("/search_book", methods=["POST"])
def search_book():
    title = request.form["title"]
    book = library.search_book(title)
    if book:
        return render_template("book_details.html", book=book)
    else:
        return "Book not found", 404

@app.route("/book_details/<isbn>")
def book_details(isbn):
    book = library.search_book(isbn)
    if book:
        return render_template("book_details.html", book=book)
    else:
        return "Book not found", 404

@app.route("/add_borrower", methods=["POST"])
def add_borrower():
    name = request.form["name"]
    email = request.form["email"]
    library.add_borrower(name, email)
    return redirect(url_for("index"))

@app.route("/remove_borrower", methods=["POST"])
def remove_borrower():
    email = request.form["email"]
    library.remove_borrower(email)
    return redirect(url_for("index"))

@app.route("/borrow_book", methods=["POST"])
def borrow_book():
    isbn = request.form["isbn"]
    email = request.form["email"]
    library.borrow_book(isbn, email)
    return redirect(url_for("index"))

@app.route("/return_book", methods=["POST"])
def return_book():
    isbn = request.form["isbn"]
    email = request.form["email"]
    library.return_book(isbn, email)
    return redirect(url_for("index"))

@app.route("/display_books")
def display_books():
    books = library.display_books()
    return render_template("book_list.html", books=books)

@app.route("/book_list")
def book_list():
    books = library.display_books()
    return render_template("book_list.html", books=books)

@app.route("/display_borrowers")
def display_borrowers():
    borrowers = library.display_borrowers()
    return render_template("borrower_list.html", borrowers=borrowers)

@app.route("/borrower_list")
def borrower_list():
    borrowers = library.display_borrowers()
    return render_template("borrower_list.html", borrowers=borrowers)

if __name__ == "__main__":
    app.run(debug=True)