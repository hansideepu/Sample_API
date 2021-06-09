from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def api():
    return "Welcome to the Book Shop"


books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route("/books", methods=['GET'])
def books_all():
    return jsonify({'Books': books})


@app.route("/books/<int:id>", methods=['GET'])
def books_id(id):
    return jsonify({'Books': books[id]})


@app.route("/books", methods=['POST'])
def books_post():
    book = {'id': 3,
            'title': 'Wings of Fire',
            'author': 'A. P. J. Abdul Kalam and Arun Tiwari',
            'first_sentence': 'We are all born with a divine fire in us.',
            'published': '1999'}
    books.append(book)
    return jsonify({"New Addition": book})


if __name__ == "__main__":
    app.run()

 #host = '0.0.0.0'
