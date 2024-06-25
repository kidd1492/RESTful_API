from flask import Blueprint, render_template, request, jsonify, redirect, session
from . import db
from .models import Park, Camp, User
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from .helper import apology, api_creation

auth = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


@auth.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@auth.route('/', methods=['POST', 'GET'])
def index():
    #setup a landing page to take care of html navigation
    if request.method == "POST":
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password = request.form.get("password")
        password1 = request.form.get("password1")
        existing_user = db.session.query(User).filter_by(email=email).first()

        if existing_user:
            return apology("Already registered, please login")
        elif not email:
            return apology("Please enter a valid email")
        elif len(user_name) < 3:
            return apology("username must be 3 characters")
        elif len(password) < 6:
            return apology("password must be 6 characters")
        elif password != password1:
            return apology("Passwords must match")
        else:
            api_key = api_creation()
            new_user = User(email=email, password=generate_password_hash(password), user_name=user_name, api_key=api_key)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")
    return render_template("index.html")


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.query(User).filter_by(email=email).first()
        if not email:
            return apology("Please enter a valid email")
        elif len(password) < 6:
            return apology("password must be 6 characters")
        elif not user:
            return apology("Email must match")
        elif not check_password_hash(user.password, password):
            return apology("incorrect password")
        else:
            # Remember which user has logged in
            api_key = user.api_key
            session["user_id"] = user.id
            return render_template("api.html", api_key=api_key)

    return render_template("login.html")


@auth.route("/logout")
def logout():
    """Log user out"""
    session.clear()

    # Redirect user home page
    return redirect("/")


@auth.route("/api")
@login_required
def api():
    user_id = session.get("user_id")
    user = db.session.query(User).filter_by(id=user_id).first()
    api_key = user.api_key
    return render_template('api.html', api_key=api_key)


@auth.route('/update_api_key', methods=["GET", "PUT"])
@login_required
def update_api_key():
    if request.method == 'PUT':
        api_key = api_creation()
        
        # Update the user's API key in the database
        user_id = session.get("user_id")
        user = db.session.query(User).filter_by(id=user_id).first()
        user.api_key = api_key
        db.session.commit()

        return render_template('api.html', api_key=api_key)
    return render_template('api.html')


''' This is the route that will give the results for a html page'''
@auth.route('/parks')
def parks():
    parks = db.session.query(Park).all()
    return render_template("results.html", parks=parks)


@auth.route('/camps')
def camps():
    camps = db.session.query(Camp).all()
    return render_template("camp_results.html", camps=camps)



@auth.route('/documentation')
def documentation():
    return render_template('documentation.html')