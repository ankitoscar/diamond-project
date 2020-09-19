

# ---------------------------------------------------------------------------- #
#                                    IMPORTS                                   #
# ---------------------------------------------------------------------------- #




# --------------------- Imported the app from the package -------------------- #
from main import app


# ------------------- Imported necessary methods from flask ------------------ #
from flask import render_template, flash, redirect, url_for, request


# ------------------- Imported the password hashing modules ------------------ #
from werkzeug.security import generate_password_hash, check_password_hash


# ---------------------------- Imported the models --------------------------- #
from main.models import User


# ---------------------------- Imported the froms ---------------------------- #
from main.forms import signinform, signupform, updateform, exploreform, exploreform2, exploreform3


#------------------------ imported flask login modules ----------------------- #
from flask_login import login_user, current_user, logout_user, login_required


# ------------------ imported current user from flask login ------------------ #
from flask_login import current_user


# ---------------------- Imported db from init, package ---------------------- #
from main import db

# ------------------------- Imported secrets token and os module for the profile_picture section below  ------------------------------------------------- #

import secrets
import os
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------- #



#login required comes with a link in init file
#login required prevents to gain access if not logged in  --> basically not letting people to access home, about, profile, explore, etc.

#is authenticated prevents to gain access if logged in --> basically not letting people to access signin or singup pages


# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #








# ---------------------------------------------------------------------------- #
#                                    ROUTES                                    #
# ---------------------------------------------------------------------------- #




# ----------------------------- Start Page Route ----------------------------- #
@app.route("/")
@app.route("/start")
def start():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template("start.html", title_given="Start")
    
    
    
# ---------------------------------------------------------------------------- #



# ------------------------------ Home Page Route ----------------------------- #
@app.route("/home")
@login_required
def home():

    
    return render_template("home.html", title_given="Home")
    
    
    
# ---------------------------------------------------------------------------- #



# ----------------------------- About Page Route ----------------------------- #
@app.route("/about")
@login_required
def about():
    return render_template("about.html", title_given="About")
    
    
    
# ---------------------------------------------------------------------------- #



# ---------------------------- Explore Page Route ---------------------------- #
@app.route("/explore" , methods=['GET', 'POST'])
@login_required
def explore():
    yy = os.getcwd()
    xx = os.path.join(yy,'main\static\diamonds.csv')
    
    df = pd.read_csv(xx, error_bad_lines=False)
    df.drop(['depth','table','Unnamed: 0'],axis = 1, inplace = True)
    df = df.sample(frac = 1)
    
    from sklearn.compose import make_column_transformer
    from sklearn.preprocessing import OneHotEncoder
    column = make_column_transformer((OneHotEncoder(drop = 'first',sparse = False),['cut','color','clarity']),remainder = 'passthrough')

    X = df.drop('price',axis = 1)
    y = df.price

    from sklearn.pipeline import make_pipeline
    from sklearn.ensemble import RandomForestRegressor
    model = make_pipeline(column,RandomForestRegressor  ())

    model.fit(X,y)









    df = {
        'carat':float(current_user.carat),
        'cut':current_user.cut,
        'color':current_user.color,
        'clarity':current_user.clarity,
        'x':float(current_user.length),
        'y':float(current_user.width),
        'z':float(current_user.depth)
    }

    


    value= current_user.cut

    columns = ['carat', 'cut', 'color', 'clarity',  'x', 'y', 'z']

    data = pd.DataFrame(df,index = [0],columns =    columns)

    output = model.predict(data)[0]


    return render_template("explore.html", title_given="Result", output=output, value=value)








# --------------------- Change Account Details Page Route -------------------- #
@app.route("/security", methods=['GET', 'POST'])
@login_required
def security():
    form = updateform()

    
    if form.validate_on_submit():
        

        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.carat = form.carat.data
        current_user.cut = form.cut.data
        current_user.color = form.color.data
        current_user.clarity = form.clarity.data
        current_user.length = form.length.data
        current_user.depth= form.depth.data
        current_user.width = form.width.data
        db.session.commit()
        flash('Your Account Has Been Updated', 'success text-center')
        return redirect(url_for('home'))

#i dont think i neeed to keep explaining this, flask login is the best thing out there
#had to import db

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.carat.data = current_user.carat
        form.cut.data = current_user.cut
        form.color.data = current_user.color
        form.clarity.data = current_user.clarity
        form.length.data = current_user.length
        form.depth.data = current_user.depth
        form.width.data = current_user.width
        
#this just helps to autofill the data in the form incase we dont fill it 
        
    
    
        

    return render_template("security.html", title_given="Security", form=form)



# ---------------------------------------------------------------------------- #



# ---------------------------- Contact Page Route ---------------------------- #
@app.route("/contact")
@login_required
def contact():
    return render_template("contact.html", title_given="Contact")



# ---------------------------------------------------------------------------- #



# ----------------------------- SignIn Page Route ---------------------------- #
@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = signinform()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember = form.remember.data)
                return redirect(url_for('home'))
            else:
                flash ('Invalid Email Address or Password', 'danger')
        else:
                flash ('Invalid Email Address or Password', 'danger')

    return render_template("signin.html", title_given="Sign In", form=form)



# ---------------------------------------------------------------------------- #



# ----------------------------- Signup Page Route ---------------------------- #
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = signupform()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password,  carat = form.carat.data, cut = form.cut.data, color=form.color.data, clarity=form.clarity.data, length=form.length.data, depth=form.depth.data, width = form.width.data)
        db.session.add(new_user)
        db.session.commit()
        flash('New user created', 'success')
        return redirect(url_for('signin'))

        
    return render_template("signup.html", title_given="Sign Up", form=form)



# ---------------------------------------------------------------------------- #



# ---------------------------- Signout Page Route ---------------------------- #
@app.route("/signout")
@login_required
def signout():
    logout_user()
    return redirect(url_for('start'))

# ---------------------------------------------------------------------------- #
