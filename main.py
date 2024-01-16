from flask import Flask, flash, render_template, request, session, abort, redirect
import os, mysql.connector

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        return render_template('home.html')


@app.route('/login', methods=['POST'])
def login_page():
    # TODO the below are placeholders for local testing, they will be replaced w/ hashed secrets before publishing
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['username'] = request.form['username']
        session['logged_in'] = True
    else:
        flash('Invalid username or password.')
    return redirect('/')


@app.route('/logout')
def logout_page():
    if session.get('logged_in'):
        session['username'] = None
        session['logged_in'] = False
    return redirect('/')


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=8000)
