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


@app.route('/book-resort')
def book_resort():
    return render_template('book_resort.html')

@app.route('/book-fitness')
def book_fitness():
    return render_template('book_fitness.html')

@app.route('/book-party-hall')
def book_party_hall():
    return render_template('book_party_hall.html')



# Sample movie data
movies = [
    {"title": "Inception", "description": "A mind-bending thriller.", "rating": "PG-13", "timing": ["12:00 PM", "3:00 PM", "6:00 PM", "9:00 PM"]},
    {"title": "Interstellar", "description": "A journey through space and time.", "rating": "PG-13", "timing": ["1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"]},
    {"title": "Tenet", "description": "A time-bending spy thriller.", "rating": "PG-13", "timing": ["2:00 PM", "5:00 PM", "8:00 PM", "11:00 PM"]},
    {"title": "Dunkirk", "description": "A war epic.", "rating": "PG-13", "timing": ["11:00 AM", "2:00 PM", "5:00 PM", "8:00 PM"]}
]

@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
