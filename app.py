from flask import Flask, render_template, url_for
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def voyager_module():
    return render_template('index.html')

@app.route('/order-food')
def order_food():
    return render_template('order_food.html')

@app.route('/order-stationery')
def order_stationery():
    return render_template('book_stationery.html')


@app.route('/book-beauty')
def book_beauty():
    return render_template('book_beauty.html')


@app.route('/book-resort')
def book_resort():
    return render_template('book_resort.html')

@app.route('/book-fitness')
def book_fitness():
    return render_template('book_fitness.html')


@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route('/book-party-hall')
def book_party_hall():
    return render_template('book_party_hall.html')



if __name__ == '__main__':
    app.run(port=5000, debug=True)
