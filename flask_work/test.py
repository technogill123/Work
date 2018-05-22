from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os
 #app.send_static_file
 #static_url_path=''
app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def home():
    return render_template('login.html')
     
@app.route('/success/<name>')
def success(name):
  return render_template('welcome.html',name=name)
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    name = None
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
	return redirect(url_for('success', name = request.form['username']))
	
    else:
	flash('wrong password!')
        return redirect(url_for('home'))	
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='', port=4000)
