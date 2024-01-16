from flask import Flask, flash, render_template, request, session, abort, redirect
import os, mysql.connector

import redirects

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')


@app.route('/login', methods=['POST'])
def login_page():
    # TODO the below are placeholders for prelim testing, they will be replaced w/ hashed secrets before prod
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


@app.route('/redir/linkedin')
def linkedin_redir():
    return redirects.linkedin("abkslm")


@app.route('/redir/github')
def github_redir():
    return redirects.github("abkslm")


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='192.168.8.2', port=9999)
