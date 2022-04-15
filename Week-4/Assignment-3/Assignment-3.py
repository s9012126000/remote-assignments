from flask import Flask, render_template, request, redirect

import pymysql.cursors

MyDb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='assignment',
    cursorclass=pymysql.cursors.DictCursor
)

# myCursor = MyDb.cursor()
# myCursor.execute("CREATE DATABASE assignment")
# myCursor.execute("CREATE TABLE user (id INTEGER AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), password VARCHAR(255))")

DEBUG = True
PORT = 3000
HOST = '0.0.0.0'
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    cursor = MyDb.cursor()
    email = request.form['email']
    password = request.form['password']
    cursor.execute('SELECT email FROM assignment.user WHERE email=%s', (email,))
    account = cursor.fetchone()
    if account:
        return render_template('home.html', msg='Account exist')
    else:
        if email and password:
            sql = "INSERT INTO user (email, password) VALUES (%s, %s)"
            cursor.execute(sql, (email, password))
            MyDb.commit()
            return render_template('member.html', msg='Register successfully')
        else:
            return render_template('home.html', msg='Email and Password should not be empty')


@app.route('/sign_in', methods=['POST'])
def sign_in():
    cursor = MyDb.cursor()
    email = request.form['email']
    password = request.form['password']
    cursor.execute('SELECT * FROM assignment.user WHERE email = %s', (email,))
    account = cursor.fetchone()
    if email == '' or password == '':
        return render_template('home.html', msg1='Email and Password should not be empty')
    if account:
        if password == account['password'] and email == account['email']:
            return render_template('member.html', msg='Login successfully')
        else:
            return render_template('home.html', msg1='Wrong email or password')
    else:
        return render_template('home.html', msg1='Wrong email or password')


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
