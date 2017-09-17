""" This is a Coding Dojo homework assignment. """

from flask import Flask, request, redirect, render_template, session, flash
import md5
from mysqlconnection import MySQLConnector
import re
import sys

# Validation regex
NAME_REGEX = re.compile(r"^[a-zA-Z\\s]+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASS_UPPER = re.compile(r"[A-Z{1,5}]")
PASS_DIGIT = re.compile(r"\d{1,5}")

app = Flask(__name__)
mysql = MySQLConnector(app, 'wall')
app.secret_key = 'SECREEEETS'


# Render index page
@app.route('/')
def index():
    messages = mysql.query_db("SELECT * \
                               FROM users_messages \
                               ORDER BY created_at DESC")
    comments = mysql.query_db(
        "SELECT * FROM users_comments ORDER BY created_at ASC")
    if session.get('logged_in') is None:
        session['first_name'] = ''
        session['last_name'] = ''
        session['email'] = ''
        session['user_id'] = ''
        session['logged_in'] = False
        session['greeting'] = ''
    elif session['logged_in'] is True:
        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': session['email']}
        newQuery = mysql.query_db(query, data)
        session['user_id'] = newQuery[0]['id']
        session['greeting'] = greeting = 'Hello ' + \
            str(session['first_name']) + ' ' + str(session['last_name']) + '!'
    else:
        session['greeting'] = ''
    return render_template('wall.html',
                           all_messages=messages,
                           all_comments=comments,
                           first_name=session['first_name'],
                           last_name=session['last_name'],
                           greeting=session['greeting'])


# Add message using form
@app.route('/message/create', methods=['POST'])
def create_message():
    if session['logged_in'] is False:
        flash('You must be logged in to submit a new message.')
    else:
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) \
                VALUES(:user_id, :message, NOW(), NOW())"
        data = {
            'user_id': session['user_id'],
            'message': request.form['message']
        }
        mysql.query_db(query, data)
    return redirect('/')


# Add comment using form
@app.route('/comment/create', methods=['POST'])
def create_comment():
    if session['logged_in'] is False:
        flash('You must be logged in to submit a new comment.')
    else:
        query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) \
             VALUES(:message_id, :user_id, :comment, NOW(), NOW())"
        data = {
            'message_id': request.form['message_id'],
            'user_id': session['user_id'],
            'comment': request.form['comment']
        }
        mysql.query_db(query, data)
    return redirect('/')


# Generate user login page
@app.route('/user/login')
def login_user():
    session['logged_in'] = False
    return render_template('login.html', logged_in=session['logged_in'])


# Process user login
@app.route('/user/login/process', methods=["POST"])
def process_login():
    session['email'] = request.form['email']
    session['password'] = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM users WHERE email = :email"
    data = {'email': session['email']}
    newQuery = mysql.query_db(query, data)
    if len(newQuery) == 0:
        flash('That email is not in our system. \
               Please try again or register a new account.')
        return redirect('/user/login')
    elif newQuery[0]['password'] == session['password']:
        session['logged_in'] = True
        session['first_name'] = newQuery[0]['first_name']
        session['last_name'] = newQuery[0]['last_name']
        session['user_id'] = newQuery[0]['id']
        # session['email'] = newQuery[0]['email']
        return redirect('/')
    else:
        flash('Your password was incorrect. Please try again.')
        return render_template('login.html', email=session['email'])


# User log out link
@app.route('/user/logout')
def logout_user():
    session.clear()
    # session.pop('logged_in', None)
    # session.pop('greeting', None)
    return redirect('/')


# Registration form
@app.route('/user/create')
def create_user():
    # Things here
    return render_template('registration.html')


# Process registration
@app.route('/user/create/process', methods=['POST'])
def process_registration():
    session['logged_in'] = False
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    # Messy verification checks for each form field
    if len(session['email']) <= 0 \
       or len(session['first_name']) <= 0 \
       or len(session['last_name']) <= 0 \
       or len(session['password']) <= 0 \
       or len(session['confirm_password']) <= 0:
        flash('You must enter every field to continue.')
        return render_template('registration.html',
                               email=session['email'],
                               first_name=session['first_name'],
                               last_name=session['last_name'])
    elif not NAME_REGEX.match(request.form['first_name']) \
      or not NAME_REGEX.match(request.form['last_name']):
        flash('Please use only alphanumeric letters for your first and last name.')
        return render_template('registration.html',
                               email=session['email'],
                               first_name=session['first_name'],
                               last_name=session['last_name'])
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address.')
        return render_template('registration.html',
                               email=session['email'],
                               first_name=session['first_name'],
                               last_name=session['last_name'])
    elif len(session['password']) < 8:
        flash('Your password must be at least 8 characters in length.')
        return render_template('registration.html',
                               email=session['email'],
                               first_name=session['first_name'],
                               last_name=session['last_name'])
    elif not PASS_UPPER.search(session['password']):
        flash('Passwords must contain one uppercase letter and one number.')
        return render_template('registration.html',
                               email=session['email'],
                               first_name=session['first_name'],
                               last_name=session['last_name'])
    elif not PASS_DIGIT.search(session['password']):
        flash('Passwords must contain one uppercase letter and one number.')
        return render_template('registration.html',
                               email=session['email'],
                               first_name=session['first_name'],
                               last_name=session['last_name'])
    elif session['password'] != session['confirm_password']:
        flash('The passwords do not match, please try again.')
        return render_template('registration.html',
                               email=session['email'],
                               first_name=session['first_name'],
                               last_name=session['last_name'])
    # Test for valid registration
    check_email_query = "SELECT email FROM users"
    check_email = mysql.query_db(check_email_query)
    for x in range(0, len(check_email)):
        print check_email[x]['email']
        if session['email'] == check_email[x]['email']:
            flash('This email address is already registered. Please try again or login to continue.')
            return render_template('registration.html',
                                   email=session['email'],
                                   first_name=session['first_name'],
                                   last_name=session['last_name'])
    hashed_password = md5.new(request.form['password']).hexdigest()
    user_data = {
        'fname': request.form['first_name'],
        'lname': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_password
    }
    user_query = "INSERT INTO users(first_name, last_name, email, \
                                    password, created_at, updated_at) \
                                    VALUES(:fname, :lname,:email, \
                                    :password, NOW(), NOW())"
    mysql.query_db(user_query, user_data)
    flash('Your registration was successful!')
    session['logged_in'] = True
    return redirect('/')
    # return render_template('registration.html', email=session['email'], first_name=session['first_name'], last_name=session['last_name'], logged_in=session['logged_in'])


app.run(debug=True)
