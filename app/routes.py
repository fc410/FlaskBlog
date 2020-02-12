from app import app
from markdown import markdown
from flask import render_template, redirect, url_for, render_template_string, request, session
from app.blog_helpers import render_markdown
import flask
import os
import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

#home page
@app.route("/")
def home():
    return render_template('home.html')

#about page
@app.route("/about")
def about():
    return render_template('about.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.values['user_name']
        password = request.values['password']

        if request.values['user_name'] != 'admin' and request.values['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['user'] = username
            session['password'] = password
            return render_template('home.html')

    return render_template('login.html', error = error)  




#route that shows all the files in the directory
@app.route('/all')
def all():
    #TODO: figure out how to find all files 
    #in the app
    mypath = r'C:\Users\cresp\OneDrive\Desktop\bin\flask-blog\app\templates'
    
    view_data = {}
    view_data["pages"] = []
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        for file in filenames:
            view_data["pages"].append(os.path.splitext(file)[0])
    
    return render_template('all.html', data = view_data)

@app.route('/edit/<page_name>')
def edit(page_name):
    render_template('home.html')
