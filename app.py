from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/order-food')
def order_food():
    return render_template('order_food.html')

@app.route('/order-stationery')
def order_stationery():
    return render_template('order_stationery.html')

@app.route('/book-resort')
def book_resort():
    return render_template('book_resort.html')

@app.route('/book-fitness')
def book_fitness():
    return render_template('book_fitness.html')

@app.route('/book-party-hall')
def book_party_hall():
    return render_template('book_party_hall.html')

@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        reconfirm_password = request.form['reconfirm_password']
        phone = request.form['phone']

        if password != reconfirm_password:
            flash('Passwords do not match!')
            return redirect(url_for('signup'))

        if not re.match(r'^[a-zA-Z0-9]+$', username):
            flash('Username must contain only characters and numbers!')
            return redirect(url_for('signup'))

        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
            return redirect(url_for('signup'))

        if not re.match(r'\d{10}', phone):
            flash('Phone number must be 10 digits!')
            return redirect(url_for('signup'))

        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            flash('Password must contain at least 8 characters, including an uppercase letter, a number, and a special character!')
            return redirect(url_for('signup'))

        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('INSERT INTO users (username, email, password, phone) VALUES (?, ?, ?, ?)',
                      (username, email, password, phone))
            conn.commit()
            conn.close()
            flash('Successfully created your account!')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('Username already exists. Please try another one.')
            return redirect(url_for('signup'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            flash('Successfully logged in!')
            return redirect(url_for('main_page'))
        else:
            flash('Incorrect email or password!')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/main')
def main_page():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(port=5001)
