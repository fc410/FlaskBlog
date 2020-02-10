from app import app
from markdown import markdown
from flask import render_template, redirect, url_for, render_template_string, request, session
from os import listdir, walk
from os.path import isfile, join
import flask

#home page
@app.route("/")
def home():
    return render_template('base.html')

#about page
@app.route("/about")
def about():
    return render_template('about.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

#@app.route("/edit/<string:id>", methods=['GET', 'POST'])
#@is_logged_in
#def edit_article(id):

@app.route("/<view_name>")
def view_name():
    html = render_template(view_name + '.md')
    view_data = {}
    return render_template(html, view_data = session)

#route that shows all the files in the directory
@app.route('/all')
def all():
    #TODO: figure out how to find all files 
    #in the app
    mypath = r'C:\\Users\\Onedrive\\Desktop\\bin\\flask-blog'
    onlyfiles =  [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #for dirpath, dirnames, filenames in walk(mypath):

    view_data = {}
    view_data["pages"] = onlyfiles
    return render_template("all.html", data = view_data)