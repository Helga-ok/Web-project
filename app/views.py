from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from werkzeug.security import generate_password_hash, check_password_hash
#from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN


@app.before_request
def before_request():
	g.user = current_user

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'nickname':'Olga'} 
    posts = [ 
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login',methods=['GET','POST'])
def login():
    	if request.method == 'GET':
		return render_template('login.html')
	username = request.form['username']
	password = request.form['password']
	registered_user = User.query.filter_by(username=username).first()
	if not registered_user:
		flash('Username is invalid', 'error')
		return redirect(url_for('login'))
	elif not registered_user.check_password(password):
		flash('Password is invalid', 'error')
		return redirect(url_for('login'))
	login_user(registered_user)
	return redirect(request.args.get('next') or url_for('index'))
	
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))	

@app.route('user/<username>')
@login_required
def user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		flash('Username'+ user.username + 'not found')
		return redirect(url_for('index'))
	return render_template('user.html', user=user)
