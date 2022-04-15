from flask import (Flask, request,redirect,
                   render_template, make_response)
DEBUG = True
PORT = 3000
HOST = '0.0.0.0'

app = Flask(__name__)

# Assignment 1
@app.route('/')
def simple_web():
    return "Hello it's my first server!"


# Assignment 2
@app.route('/data')
def data(number=None):
    number = request.args.get('number', number)
    if number:
        try:
            int_num = int(number)
            tol = 0
            for num in range(int_num):
                tol += num+1
            return str(tol)
        except ValueError:
            return "Wrong Parameter"
    else:
        return 'Lack of Parameter'
    
    
# Assignment 3
@app.route('/sum.html')
def total():
    return render_template('sum.html')


# Assignment 4
@app.route('/myName')
def myName():
    name = request.cookies.get('userID')
    if name:
        return name
    else:
        return render_template('form.html')

@app.route('/trackName', methods = ['POST', 'GET'])
def trackName():
    name = request.form['name']
    response = make_response(redirect('/myName'))
    response.set_cookie('userID',name)
    return response


if __name__ =='__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)