from flask import Flask, redirect, url_for, request
import os


app = Flask(__name__, static_url_path='')


@app.route('/')
def home():

    return app.send_static_file('login.html')


@app.route('/welcome')
def welcome():
       username = request.cookies.get('username')
       return app.send_static_file('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        if request.form['username'] == 'admin' and request.form['password'] == 'admin':

	    resp.set_cookie('username','username')
            return redirect(url_for('welcome'),resp)

        else:

            return redirect(url_for('home'))

    


if __name__ == '__main__':
 app.run(host = '0.0.0.0',port = 5000)
